import logging
import os
import shutil
import sys
import tempfile

from pyflink.dataset import ExecutionEnvironment
from pyflink.table import BatchTableEnvironment, TableConfig, DataTypes
from pyflink.table import expressions as expr
from pyflink.table.descriptors import OldCsv, FileSystem, Schema
from pyflink.table.expressions import lit


def demo01():
    exec_env = ExecutionEnvironment.get_execution_environment()
    exec_env.set_parallelism(1)
    t_config = TableConfig()
    t_env = BatchTableEnvironment.create(exec_env, t_config)
    # StreamExecutionEnvironment

    t_env.connect(FileSystem().path(r'F:\github\openjw\penter\bigdata_study\pyflink1.x\batch\demo01\input')) \
        .with_format(OldCsv()
                     .field('word', DataTypes.STRING())) \
        .with_schema(Schema()
                     .field('word', DataTypes.STRING())) \
        .create_temporary_table('mySource')
    # 文件存在会报错
    t_env.connect(FileSystem().path(r'F:\github\openjw\penter\bigdata_study\pyflink1.x\batch\demo01\output')) \
        .with_format(OldCsv()
                     .field_delimiter('\t')
                     .field('word', DataTypes.STRING())
                     .field('count', DataTypes.BIGINT())) \
        .with_schema(Schema()
                     .field('word', DataTypes.STRING())
                     .field('count', DataTypes.BIGINT())) \
        .create_temporary_table('mySink')

    tab = t_env.from_path('mySource')
    tab.group_by(tab.word) \
        .select(tab.word, lit(1).count) \
        .execute_insert('mySink').wait()

def demo02():
    exec_env = ExecutionEnvironment.get_execution_environment()
    exec_env.set_parallelism(1)
    t_config = TableConfig()
    t_env = BatchTableEnvironment.create(exec_env, t_config)
    # StreamExecutionEnvironment

    my_source_ddl = """
        create table mySource (
            word VARCHAR
        ) with (
            'connector' = 'filesystem',
            'format.type' = 'csv',
            'connector.path' = 'F:/github/openjw/penter/bigdata_study/pyflink1.x/batch/demo01/input'
        )
    """

    my_sink_ddl = """
        create table mySink (
            word VARCHAR,
            `count` BIGINT
        ) with (
            'connector' = 'filesystem',
            'format.type' = 'csv',
            'connector.path' = 'F:/github/openjw/penter/bigdata_study/pyflink1.x/batch/demo01/output'
        )
    """

    t_env.execute_sql(my_source_ddl)
    t_env.execute_sql(my_sink_ddl)

    tab = t_env.from_path('mySource')
    tab.group_by(tab.word) \
        .select(tab.word, lit(1).count) \
        .execute_insert('mySink').wait()

if __name__ == '__main__':
    # demo01()
    demo02() # 跑不起来
