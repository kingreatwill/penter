from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings, DataTypes

# use_old_planner
from pyflink.table.expressions import row
from pyflink.table.udf import udf, ScalarFunction

f_s_env = StreamExecutionEnvironment.get_execution_environment()
f_s_settings = EnvironmentSettings.new_instance().use_old_planner().in_streaming_mode().build()
f_s_t_env = StreamTableEnvironment.create(f_s_env, environment_settings=f_s_settings)
#f_s_t_env.get_config().get_configuration().set_string()

# env = StreamExecutionEnvironment.get_execution_environment()
# table_env = StreamTableEnvironment.create(env, settings)
# # enable checkpointing
# table_env.get_config().get_configuration().set_string("execution.checkpointing.mode", "EXACTLY_ONCE")
# table_env.get_config().get_configuration().set_string("execution.checkpointing.interval", "10s")

# use_blink_planner
b_s_env = StreamExecutionEnvironment.get_execution_environment()
b_s_settings = EnvironmentSettings.new_instance().use_blink_planner().in_streaming_mode().build()
b_s_t_env = StreamTableEnvironment.create(b_s_env, environment_settings=b_s_settings)


b_s_t_env.add_python_archive("py_env.zip")
b_s_t_env.get_config().set_python_executable("py_env.zip/py_env/bin/python")
b_s_t_env.add_python_archive("py_env.zip", "myenv")
b_s_t_env.get_config().set_python_executable("myenv/py_env/bin/python")

b_s_t_env.add_python_file("")

b_s_t_env.create_java_function("func", "java.user.defined.function.class.name")
b_s_t_env.create_java_temporary_function("func", "java.user.defined.function.class.name")
b_s_t_env.create_java_temporary_system_function("func", "java.user.defined.function.class.name")


b_s_t_env.create_temporary_function( "add_one", udf(lambda i: i + 1, result_type=DataTypes.BIGINT()))
@udf(result_type=DataTypes.BIGINT())
def add(i, j):
     return i + j
b_s_t_env.create_temporary_function("add", add)

class SubtractOne(ScalarFunction):
    def eval(self, i):
        return i - 1
b_s_t_env.create_temporary_function( "subtract_one", udf(SubtractOne(), result_type=DataTypes.BIGINT()))
# create_temporary_system_function

# drop_function
# drop_temporary_function
# drop_temporary_system_function
# drop_temporary_table
# drop_temporary_view

# tab = table_env.from_path("catalogName.dbName.tableName")
# tab = table_env.from_path("catalogName.`db.Name`.`Table`")

#pdf = pd.DataFrame(np.random.rand(1000, 2))
# b_s_t_env.from_pandas(pdf, ["a", "b"])
# b_s_t_env.from_pandas(pdf, [DataTypes.DOUBLE(), DataTypes.DOUBLE()]))
# b_s_t_env.from_pandas(pdf,
#                       DataTypes.ROW([DataTypes.FIELD("a", DataTypes.DOUBLE()),
#                                      DataTypes.FIELD("b", DataTypes.DOUBLE())]))

# use the second parameter to specify custom field names
b_s_t_env.from_elements([(1, 'Hi'), (2, 'Hello')], ['a', 'b'])
# use the second parameter to specify custom table schema
b_s_t_env.from_elements([(1, 'Hi'), (2, 'Hello')],
                        DataTypes.ROW([DataTypes.FIELD("a", DataTypes.INT()),
                                       DataTypes.FIELD("b", DataTypes.STRING())]))
# use the thrid parameter to switch whether to verify the elements against the schema
b_s_t_env.from_elements([(1, 'Hi'), (2, 'Hello')],
                        DataTypes.ROW([DataTypes.FIELD("a", DataTypes.INT()),
                                       DataTypes.FIELD("b", DataTypes.STRING())]),
                        False)
# create Table from expressions
b_s_t_env.from_elements([row(1, 'abc', 2.0), row(2, 'def', 3.0)],
                        DataTypes.ROW([DataTypes.FIELD("a", DataTypes.INT()),
                                       DataTypes.FIELD("b", DataTypes.STRING()),
                                       DataTypes.FIELD("c", DataTypes.FLOAT())]))


# table
# 链接一个table
b_s_t_env.connect(...).create_temporary_table("table1")
sink_ddl = """
        create table table1(
            word VARCHAR,
            `count` BIGINT
        ) with (
            'connector.type' = 'filesystem',
            'format.type' = 'csv',
            'connector.path' = '{}'
        )
        """.format("/tmp/xxx")
b_s_t_env.execute_sql(sink_ddl)

# 查询
proj_table  = b_s_t_env.from_path("table1").select(...)
# 存为另一个table
b_s_t_env.register_table("projectedTable", proj_table)
b_s_t_env.create_temporary_view("projectedTable", proj_table)
# 永久table
b_s_t_env.use_catalog("custom_catalog")
b_s_t_env.use_database("custom_database")
"""
// register the view named 'exampleView' in the catalog named 'custom_catalog'
// in the database named 'custom_database' 
tableEnv.createTemporaryView("exampleView", table);

// register the view named 'exampleView' in the catalog named 'custom_catalog'
// in the database named 'other_database' 
tableEnv.createTemporaryView("other_database.exampleView", table);

# 这里要注意有个`
// register the view named 'example.View' in the catalog named 'custom_catalog'
// in the database named 'custom_database' 
tableEnv.createTemporaryView("`example.View`", table);

// register the view named 'exampleView' in the catalog named 'other_catalog'
// in the database named 'other_database' 
tableEnv.createTemporaryView("other_catalog.other_database.exampleView", table);
"""
# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/common.html#create-a-view-from-a-datastream-or-dataset
# 从DataStream 创建视图和table
"""
// get StreamTableEnvironment
// registration of a DataSet in a BatchTableEnvironment is equivalent
StreamTableEnvironment tableEnv = ...; // see "Create a TableEnvironment" section

DataStream<Tuple2<Long, String>> stream = ...

// register the DataStream as View "myTable" with fields "f0", "f1"
tableEnv.createTemporaryView("myTable", stream);

// register the DataStream as View "myTable2" with fields "myLong", "myString"
tableEnv.createTemporaryView("myTable2", stream, $("myLong"), $("myString"));


// get StreamTableEnvironment
// registration of a DataSet in a BatchTableEnvironment is equivalent
StreamTableEnvironment tableEnv = ...; // see "Create a TableEnvironment" section

DataStream<Tuple2<Long, String>> stream = ...

// Convert the DataStream into a Table with default fields "f0", "f1"
Table table1 = tableEnv.fromDataStream(stream);

// Convert the DataStream into a Table with fields "myLong", "myString"
Table table2 = tableEnv.fromDataStream(stream, $("myLong"), $("myString"));
"""
# table 转 ds
b_s_t_env.to_append_stream()

# 执行计划
env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

table1 = t_env.from_elements([(1, "hello")], ["count", "word"])
table2 = t_env.from_elements([(1, "hello")], ["count", "word"])
table = table1 \
    .where(table1.word.like('F%')) \
    .union_all(table2)
print(table.explain())