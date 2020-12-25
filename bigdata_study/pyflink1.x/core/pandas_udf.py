# https://ci.apache.org/projects/flink/flink-docs-release-1.12/zh/dev/python/table-api-users-guide/conversion_of_pandas.html#%E5%B0%86pyflink%E8%A1%A8%E8%BD%AC%E6%8D%A2%E4%B8%BApandas-dataframe
if __name__ == '__main__':
    ...
"""
import pandas as pd
import numpy as np

# 创建一个Pandas DataFrame
pdf = pd.DataFrame(np.random.rand(1000, 2))

# 由Pandas DataFrame创建PyFlink表
table = t_env.from_pandas(pdf)

# 由Pandas DataFrame创建指定列名的PyFlink表
table = t_env.from_pandas(pdf, ['f0', 'f1'])

# 由Pandas DataFrame创建指定列类型的PyFlink表
table = t_env.from_pandas(pdf, [DataTypes.DOUBLE(), DataTypes.DOUBLE()])

# 由Pandas DataFrame创建列名和列类型的PyFlink表
table = t_env.from_pandas(pdf,
                          DataTypes.ROW([DataTypes.FIELD("f0", DataTypes.DOUBLE()),
                                         DataTypes.FIELD("f1", DataTypes.DOUBLE())])
"""

"""
import pandas as pd
import numpy as np

# 创建PyFlink Table
pdf = pd.DataFrame(np.random.rand(1000, 2))
table = t_env.from_pandas(pdf, ["a", "b"]).filter("a > 0.5")

# 转换PyFlink Table为Pandas DataFrame
# 这意味着需要把表的内容收集到客户端，因此在调用此函数之前，请确保表的内容可以容纳在内存中。
# https://ci.apache.org/projects/flink/flink-docs-release-1.12/zh/dev/python/python_config.html#python-fn-execution-arrow-batch-size
# python.fn-execution.arrow.batch.size  10000
pdf = table.to_pandas()
# 通过Table.limit，设置收集到客户端的数据的条数。
pdf = table.limit(100).to_pandas()
"""

"""
import pandas as pd
from scipy import stats
from pyflink.table import DataTypes
from pyflink.table.udf import udf

@udf(input_types=[DataTypes.DOUBLE()],result_type=DataTypes.DOUBLE(),udf_type="pandas")
def cdf(v):
    return pd.Series(stats.norm.cdf(v))

"""