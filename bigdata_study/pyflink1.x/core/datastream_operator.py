from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, CoMapFunction, CoFlatMapFunction
from pyflink.datastream.connectors import StreamingFileSink, DefaultRollingPolicy, OutputFileConfig
from pyflink.common import Row

class MyCoMapFunction(CoMapFunction):

    def map1(self, element):
        return element[0] #str(value[0] + 1)

    def map2(self, element):
        return element[0]

class MyCoFlatMapFunction(CoFlatMapFunction):

    def flat_map1(self, element):
        for i in range(element):
            yield i

    def flat_map2(self, element):
        for i in range(element):
            yield i

def connect_operators():
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_parallelism(1)
    s_env.set_python_executable(r"D:/ProgramData/Anaconda3/envs/penter/python.exe")
    ds1 = s_env.from_collection([(1, 'Hi', 'Hello'), (2, 'Hello', 'Hi')], type_info=Types.ROW( [Types.INT(), Types.STRING(), Types.STRING()]))
    ds2 = s_env.from_collection([(3, 'Hi2', 'Hello2'), (4, 'Hello2', 'Hi2')], type_info=Types.ROW([Types.INT(), Types.STRING(), Types.STRING()]))

    # Connect DataStream,DataStream → ConnectedStreams
    #cs = ds1.connect(ds2).map(MyCoMapFunction()) # , output_type=Types.INT()
    cs = ds1.connect(ds2).flat_map(MyCoFlatMapFunction())# , output_type=Types.INT()
    cs.add_sink(StreamingFileSink.for_row_format('/tmp/output', SimpleStringEncoder()).build())
    print(s_env.get_execution_plan())
    #s_env.execute('connect_operators')

def ds_operators():
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_parallelism(1)
    s_env.set_python_executable(r"D:/ProgramData/Anaconda3/envs/penter/python.exe")
    ds = s_env.from_collection([(1, 'Hi', 'Hello'), (2, 'Hello', 'Hi')], type_info=Types.ROW( [Types.INT(), Types.STRING(), Types.STRING()]))
    """
    map
    flat_map
    filter
    key_by DataStream → KeyedStream
    reduce KeyedStream → DataStream
    union DataStream* → DataStream
    connect DataStream,DataStream → ConnectedStreams
    转换元组：
    project
    分区：
    partition_custom 自定义分区
    shuffle 随机分区 根据均匀分布随机划分元素。
    rebalance 轮询分区
    rescale 重新分区
    broadcast 向每个分区广播元素
    随意定制
    process 只有在KeyedStream上应用ProcessFunction时，才可以访问键控状态和计时器TimerService(相当于java的windows)。
    其它
    start_new_chain
    disable_chaining
    slot_sharing_group
    """
    ds.rescale()
    ds.map()
    ds.flat_map()
    ds.filter()
    # KeyBy DataStream → KeyedStream
    # Reduce KeyedStream → DataStream
    ds = s_env.from_collection([(1, 'a'), (2, 'a'), (3, 'a'), (4, 'b')],
                                  type_info=Types.ROW([Types.INT(), Types.STRING()]))
    ds.key_by(lambda a: a[1]) \
        .reduce(lambda a, b: Row(a[0] + b[0], b[1]))
    # 广播
    ds.broadcast()
    # project 只有元组ds才可以
    ds = s_env.from_collection([[1, 2, 3, 4], [5, 6, 7, 8]],
                               type_info=Types.TUPLE(
                                   [Types.INT(), Types.INT(), Types.INT(), Types.INT()]))
    # 输出元组的1,3索引
    ds.project(1, 3).map(lambda x: (x[0], x[1] + 1)).add_sink()

    # 存储
    ds.add_sink(
        StreamingFileSink.for_row_format('/tmp/output', SimpleStringEncoder())
            .with_rolling_policy(
            DefaultRollingPolicy.builder().with_rollover_interval(15 * 60 * 1000)
                .with_inactivity_interval(5 * 60 * 1000)
                .with_max_part_size(1024 * 1024 * 1024).build())
            .with_output_file_config(
            OutputFileConfig.OutputFileConfigBuilder()
                .with_part_prefix("prefix")
                .with_part_suffix("suffix").build()).build()
    )
    s_env.execute('ds_operators')

# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/stream/operators/
if __name__ == '__main__':
    connect_operators()