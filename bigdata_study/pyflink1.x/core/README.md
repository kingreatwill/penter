
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