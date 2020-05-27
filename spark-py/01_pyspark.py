# 实现pandas DataFrame 和spark dataFrame 相互转换
import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("dataFrame") \
    .getOrCreate()
# Loads data.


ll3 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])

cc = ll3.values.tolist()

dd = list(ll3.columns)
# df=spark.createDataFrame(ll3)

# turn pandas.DataFrame  to spark.dataFrame
spark_df = spark.createDataFrame(cc, dd)

print('spark.dataFram=', spark_df.show())

# turn spark.dataFrame to pandas.DataFrame
pandas_df = spark_df.toPandas()

print('pandas.DataFrame=', pandas_df)
