from pyflink.table import *
from pyflink.table.expressions import col, lit, concat
from pyflink.table.window import Tumble


def demo01():
    # environment configuration
    t_env = BatchTableEnvironment.create(environment_settings=EnvironmentSettings.new_instance().in_batch_mode().use_blink_planner().build())

    # register Orders table and Result table sink in table environment
    source_data_path = "/path/to/source/directory/"
    result_data_path = "/path/to/result/directory/"
    source_ddl = f"""
            create table Orders(
                a VARCHAR,
                b BIGINT,
                c BIGINT,
                rowtime TIMESTAMP(3),
                WATERMARK FOR rowtime AS rowtime - INTERVAL '1' SECOND
            ) with (
                'connector' = 'filesystem',
                'format' = 'csv',
                'path' = '{source_data_path}'
            )
            """
    t_env.execute_sql(source_ddl)

    sink_ddl = f"""
        create table `Result`(
            a VARCHAR,
            cnt BIGINT
        ) with (
            'connector' = 'filesystem',
            'format' = 'csv',
            'path' = '{result_data_path}'
        )
        """
    t_env.execute_sql(sink_ddl)

    # specify table program
    orders = t_env.from_path("Orders")  # schema (a, b, c, rowtime)

    orders.group_by("a").select(orders.a, orders.b.count.alias('cnt')).execute_insert("result").wait()

    orders.where(orders.a == 'red')
    orders.filter(orders.b % 2 == 0)
    orders.add_columns(concat(orders.c, 'sunny'))
    orders.add_or_replace_columns(concat(orders.c, 'sunny').alias('desc'))
    orders.drop_columns(orders.b, orders.c)
    orders.rename_columns(orders.b.alias('b2'), orders.c.alias('c2'))
    orders.group_by(orders.a).select(orders.a, orders.b.sum.alias('d'))

    # tab.group_by(tab.key).select(tab.key, tab.value.avg.alias('average'))
    # tab.group_by("key").select("key, value.avg as average")
    result = orders.filter(orders.a.is_not_null & orders.b.is_not_null & orders.c.is_not_null) \
        .select(orders.a.lower_case.alias('a'), orders.b, orders.rowtime) \
        .window(Tumble.over(lit(1).hour).on(orders.rowtime).alias("hourly_window")) \
        .group_by(col('hourly_window'), col('a')) \
        .select(col('a'), col('hourly_window').end.alias('hour'), col('b').avg.alias('avg_billing_amount'))
    """
    SELECT user, SUM(amount)
    FROM Orders
    GROUP BY TUMBLE(rowtime, INTERVAL '1' DAY), user
    """


# SQL内置函数：https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/functions/systemFunctions.html
# SQL Data类型：https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/types.html
# table operator对应的sql：https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/sql/queries.html
# 各种Window 写法;https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/tableApi.html#group-windows

# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/tableApi.html
# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/python/table-api-users-guide/operations.html
if __name__ == '__main__':
    demo01()