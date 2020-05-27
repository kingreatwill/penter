import os
import sys

import pandas as pd
import numpy as np
import databricks.koalas as ks
from pyspark.sql import SparkSession
# https://koalas.readthedocs.io/en/latest/getting_started/10min.html

# os.environ['PYSPARK_PYTHON'] = "python3"
# os.environ['PYSPARK_DRIVER_PYTHON'] = "python3"

# os.environ['SPARK_HOME'] = r'E:\bigdata\spark-2.4.4-bin-hadoop2.7'
# sys.path.append(r'E:\bigdata\spark-2.4.4-bin-hadoop2.7\python')
s = ks.Series([1, 3, 5, np.nan, 6, 8])

print(s)

"""
koalas项目通过在Apache Spark上实现panda DataFrame API，使数据科学家在与大数据交互时更高效。
panda是Python中事实上的标准(单节点)DataFrame实现，而Spark是大数据处理的事实上的标准。
有了这个包，你可以:
如果你对panda已经很熟悉了，那就用Spark来提高效率吧，不需要学习曲线。
有一个单独的代码基，它既可以使用panda(测试、较小的数据集)，也可以使用Spark(分布式数据集)。
该项目目前处于beta测试阶段，并且正在快速发展，每两周发布一次。
"""
# spark.DataFrane分布式转pandas.dataframe
# import pandas as pd
#
#
# def _map_to_pandas(rdds):
#     return [pd.DataFrame(list(rdds))]
#
#
# def topas(df, n_partitions=None):
#     if n_partitions is not None: df = df.repartition(n_partitions)
#     df_pand = df.rdd.mapPartitions(_map_to_pandas).collect()
#     df_pand = pd.concat(df_pand)
#     df_pand.columns = df.columns
#     return df_pand
#
#
# # pandas_df = topas(spark_df)
