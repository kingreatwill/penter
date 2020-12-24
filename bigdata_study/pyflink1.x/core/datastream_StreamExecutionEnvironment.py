from pyflink.common import ExecutionMode, RestartStrategies
from pyflink.common.serialization import JsonRowDeserializationSchema
from pyflink.common.typeinfo import Types
from pyflink.dataset import ExecutionEnvironment
from pyflink.datastream import StreamExecutionEnvironment, CheckpointingMode, ExternalizedCheckpointCleanup, TimeCharacteristic, RocksDBStateBackend
from pyflink.datastream.connectors import FlinkKafkaConsumer


def demo01():
    # 创建一个执行环境，该环境表示程序当前正在执行。如果程序是独立调用的，则方法返回本地执行环境。
    # 1：创建一个流处理的执行环境，如果在本地启动则创建本地执行环境，如果在集群启动则创建集群执行环境
    env = StreamExecutionEnvironment.get_execution_environment()


    # 添加添加到程序的每个用户代码类加载器的类路径中的url列表。路径必须指定一个协议(例如file://)，并且可以在所有节点上访问
    env.add_classpaths("file://lib")

    # 添加将被上传到集群并由作业引用的jar文件列表。 .set_string("pipeline.jars", 'file://' + dir_kafka_sql_connect)
    env.add_jars("file://jars")

    # 添加python存档文件。该文件将被解压到python UDF worker的工作目录中。
    # 目前只支持zip格式,例如zip、jar、whl、egg等
    # 会先解压zip -r py_env.zip py_env.zip
    env.add_python_archive("py_env.zip")
    # 如果python UDF依赖于集群中不存在的特定python版本，则可以使用此方法上传虚拟环境。注意，上传环境中包含的python解释器的路径应该通过该方法指定
    env.set_python_executable("py_env.zip/py_env/bin/python")
    # con/flink-conf.yaml 添加 python.client.executable: /usr/bin/python3
    # or
    env.add_python_archive("py_env.zip", "myenv")
    env.set_python_executable("myenv/py_env/bin/python")
    # the files contained in the archive file can be accessed in UDF
    """
    def my_udf():
        with open("myenv/py_env/data/data.txt") as f:
            ...
    """
    # 相当于 pip download -d cached_dir -r requirements.txt --no-binary :all:
    env.set_python_requirements("requirements.txt", "cached_dir")
    # 添加一个python依赖项，它可以是python文件、python包或本地目录。它们将被添加到python UDF工作者的PYTHONPATH中。请确保可以导入这些依赖项。
    env.add_python_file("")

    # 添加source
    #1. add_source
    ds = env.add_source(
        FlinkKafkaConsumer(
            "source_topic",
            JsonRowDeserializationSchema.builder().type_info(type_info=Types.ROW([Types.INT(), Types.STRING()])).build(),
            {'bootstrap.servers': 'localhost:9092', 'group.id': 'test_group'})
    )
    # 2. from_collection
    ds = env.from_collection([1,2,3,], Types.INT())
    # 3. 从文件
    ds = env.read_text_file("hdfs://host:port/file/path")

    # 禁用operator chaining
    env.disable_operator_chaining()

    """
    Flink 可以非常高效的进行有状态流的计算，通过使用 Flink 内置的 Keyed State 和 Operator State，保存每个算子的状态。
    默认情况下，状态是存储在 JVM 的堆内存中，如果系统中某个环节发生了错误，宕机，这个时候所有的状态都会丢失，并且无法恢复，会导致整个系统的数据计算发生错误。
    此时就需要 Checkpoint 来保障系统的容错。Checkpoint 过程，就是把算子的状态周期性持久化的过程。
    在系统出错后恢复时，就可以从 checkpoint 中恢复每个算子的状态，从上次消费的地方重新开始消费和计算。从而可以做到在高效进行计算的同时还可以保证数据不丢失，只计算一次。
    
    最少一次
    AT_LEAST_ONCE
    如果假定是传输过程出现问题，而服务器没有收到数据，这样time out之后重传数据。但这可能是返回成功消息的时候出问题，而此时服务器已经收到数据，这样会因为重传而收到多份数据，这就是 at least once
    
    严格一次
    EXACTLY_ONCE
    
    最多一次（At-most-once）、最少一次（At-least-once），以及严格一次（Exactly-once）
    
    Checkpoint 必要的两个条件
    1. 需要支持重放一定时间范围内数据的数据源，比如：kafka 。
    因为容错机制就是在任务失败后自动从最近一次成功的 checkpoint 处恢复任务，此时需要把任务失败前消费的数据再消费一遍。
    假设数据源不支持重放，那么数据还未写到存储中就丢了，任务恢复后，就再也无法重新消费这部分丢了的数据了。
    
    2. 需要一个存储来保存持久化的状态，如：Hdfs，本地文件。可以在任务失败后，从存储中恢复 checkpoint 数据。
    
    https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/stream/state/checkpointing.html
    https://ci.apache.org/projects/flink/flink-docs-release-1.12/api/python/pyflink.datastream.html#pyflink.datastream.CheckpointConfig
    """
    # 每 300s 做一次 checkpoint
    env.enable_checkpointing(300000, CheckpointingMode.AT_LEAST_ONCE)
    # MemoryStateBackend FsStateBackend CustomStateBackend
    env.set_state_backend(RocksDBStateBackend("file://var/checkpoints/"))

    # set mode to exactly-once (this is the default)
    env.get_checkpoint_config().set_checkpointing_mode(CheckpointingMode.EXACTLY_ONCE)

    # 两次 checkpoint 的间隔时间至少为 500ms，默认是 0，立即进行下一次 checkpoint make sure 500 ms of progress happen between checkpoints
    env.get_checkpoint_config().set_min_pause_between_checkpoints(500)

    # checkpoint 必须在 60s 内结束，否则被丢弃 checkpoints have to complete within one minute, or are discarded
    env.get_checkpoint_config().set_checkpoint_timeout(60000)

    # 同一时间只能允许有一个 checkpoint allow only one checkpoint to be in progress at the same time
    env.get_checkpoint_config().set_max_concurrent_checkpoints(1)

    # 当 Flink 任务取消时，保留外部保存的 checkpoint 信息 enable externalized checkpoints which are retained after job cancellation
    env.get_checkpoint_config().enable_externalized_checkpoints(ExternalizedCheckpointCleanup.RETAIN_ON_CANCELLATION)

    # 当有较新的 Savepoint 时，作业也会从 Checkpoint 处恢复 allow job recovery fallback to checkpoint when there is a more recent savepoint
    env.get_checkpoint_config().set_prefer_checkpoint_for_recovery(True)

    # 允许实验性的功能：非对齐的 checkpoint，以提升性能 enables the  experimental  unaligned checkpoints
    #  CheckpointingMode.EXACTLY_ONCE时才能启用
    env.get_checkpoint_config().enable_unaligned_checkpoints()
    # env.get_checkpoint_config().disable_unaligned_checkpoints() 等同env.get_checkpoint_config().enable_unaligned_checkpoints(False)

    env.get_checkpoint_interval() #等同 env.get_checkpoint_config().get_checkpoint_interval()


    """
    """
    # https://ci.apache.org/projects/flink/flink-docs-release-1.12/api/python/pyflink.common.html#pyflink.common.ExecutionConfig
    # bin/flink run -Dexecution.runtime-mode=BATCH examples/streaming/WordCount.jar
    env.get_config().set_execution_mode(ExecutionMode.BATCH)

    env.get_config().disable_auto_generated_uids()# enable_auto_generated_uids
    # 自己设置uid
    ds.uid("xx")

    # 设置从此环境创建的所有流的时间特性，例如，处理时间、事件时间或摄取时间。
    # 如果将特征设置为EventTime的incertiontime，则将设置默认值水印更新间隔为200毫秒。
    env.set_stream_time_characteristic(TimeCharacteristic.EventTime) #设置时间分配器
    env.get_config().set_auto_watermark_interval(200) # 每200ms发出一个watermark

    env.get_config().set_global_job_parameters({"environment.checkpoint_interval": "1000"})

    env.get_config().set_restart_strategy(RestartStrategies.fixed_delay_restart(10, 1000))


    # 执行
    env.execute("job name")
    # 异步执行
    jobClient = env.execute_async("job name")
    jobClient.get_job_execution_result().result()


    """
    设置输出缓冲区刷新的最大时间频率(毫秒)。默认情况下，输出缓冲区会频繁刷新，以提供较低的延迟，并帮助流畅的开发人员体验。设置该参数可以产生三种逻辑模式:
    正整数触发该整数周期性刷新
    0 触发每个记录之后的刷新，从而最大限度地减少延迟(最好不要设置为0 可以设置一个接近0的数值，比如5或者10)
    -1 仅在输出缓冲区已满时才触发刷新，从而最大化吞吐量
    """
    # 输出缓冲区刷新的最大时间频率(毫秒)
    env.get_buffer_timeout()
    env.set_buffer_timeout(10)

    # 获取执行计划的json，复制到https://flink.apache.org/visualizer/
    env.get_execution_plan()





# https://ci.apache.org/projects/flink/flink-docs-release-1.12/api/python/pyflink.datastream.html
if __name__ == '__main__':
    demo01()