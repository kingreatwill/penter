
本地交互环境
./pyflink-shell.sh local


为了使流批一体，flink不推荐使用dataset来处理批
https://cwiki.apache.org/confluence/display/FLINK/FLIP-134%3A+Batch+execution+for+the+DataStream+API
```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
env.setRuntimeMode(RuntimeMode.BATCH);
Configuration conf = new Configuration();
conf.setString("execution.shuffle-mode", "ALL_EDGES_BLOCKING");
env.configure(conf);
```

```python

f_s_env = StreamExecutionEnvironment.get_execution_environment()
f_s_settings = EnvironmentSettings.new_instance().use_old_planner().in_streaming_mode().build()
f_s_t_env = StreamTableEnvironment.create(f_s_env, environment_settings=f_s_settings)
```

https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/python/python_config.html
python执行分为 
python.client.executable （PYFLINK_CLIENT_EXECUTABLE） 优先级，1.配置 'python.client.executable'在代码中；2.环境变量；3.con/flink-conf.yaml 添加 python.client.executable: /usr/bin/python3


和python.executable （python UDF worker） 可以通过-pyexec

t_config.set_python_executable("/opt/python38/bin/python3")

zip -r venv.zip venv
bin/flink run -m yarn-cluster -pyarch venv.zip -pyexec venv.zip/venv/bin/Python -py deploy_demo.py

-pyexec指定 venv.zip 中的 Python 解释器来执行 Python UDF，路径需要和 zip 包内部结构一致。

## REST API
https://ci.apache.org/projects/flink/flink-docs-release-1.12/ops/rest_api.html
## Metrics
https://ci.apache.org/projects/flink/flink-docs-release-1.12/ops/metrics.html

Request metrics for a specific entity:

/jobmanager/metrics
/taskmanagers/<taskmanagerid>/metrics
/jobs/<jobid>/metrics
/jobs/<jobid>/vertices/<vertexid>/subtasks/<subtaskindex>
Request metrics aggregated across all entities of the respective type:

/taskmanagers/metrics
/jobs/metrics
/jobs/<jobid>/vertices/<vertexid>/subtasks/metrics
Request metrics aggregated over a subset of all entities of the respective type:

/taskmanagers/metrics?taskmanagers=A,B,C
/jobs/metrics?jobs=D,E,F
/jobs/<jobid>/vertices/<vertexid>/subtasks/metrics?subtask=1,2,3

## Window
https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/sql/queries.html#group-windows


## 从Cassandra读取数据
https://stackoverflow.com/questions/42617575/read-write-data-into-cassandra-using-apache-flink-java-api
https://www.99opts.com/cassandra-source-to-retrieve-data-for-specific-data-types-with-apache-flink/