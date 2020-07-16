#!/usr/bin/env python
# encoding=utf8
# Spark Mlib实战（逻辑回归）根据美国CDC公布的新生儿存活率数据，预测新生儿存活率。
# =========================== phase 1：数据清洗 ======================================
#
#  注释说明 ''' 为代码说明或测试  #正常代码 ，因为结果已经算出，不需在重新跑了。
#
import pyspark.sql.types as typ
from pyspark.sql import SparkSession
import chardet
import sys

# reload(sys)
# sys.setdefaultencoding('ISO-8859-1')
datafile = 'births_train.csv'
# print sys.getdefaultencoding()
labels = [
    ('INFANT_ALIVE_AT_REPORT', typ.StringType()),
    ('BIRTH_YEAR', typ.IntegerType()),
    ('BIRTH_MONTH', typ.IntegerType()),
    ('BIRTH_PLACE', typ.StringType()),
    ('MOTHER_AGE_YEARS', typ.IntegerType()),
    ('MOTHER_RACE_6CODE', typ.StringType()),
    ('MOTHER_EDUCATION', typ.StringType()),
    ('FATHER_COMBINED_AGE', typ.IntegerType()),
    ('FATHER_EDUCATION', typ.StringType()),
    ('MONTH_PRECARE_RECODE', typ.StringType()),
    ('CIG_BEFORE', typ.IntegerType()),
    ('CIG_1_TRI', typ.IntegerType()),
    ('CIG_2_TRI', typ.IntegerType()),
    ('CIG_3_TRI', typ.IntegerType()),
    ('MOTHER_HEIGHT_IN', typ.IntegerType()),
    ('MOTHER_BMI_RECODE', typ.IntegerType()),
    ('MOTHER_PRE_WEIGHT', typ.IntegerType()),
    ('MOTHER_DELIVERY_WEIGHT', typ.IntegerType()),
    ('MOTHER_WEIGHT_GAIN', typ.IntegerType()),
    ('DIABETES_PRE', typ.StringType()),
    ('DIABETES_GEST', typ.StringType()),
    ('HYP_TENS_PRE', typ.StringType()),
    ('HYP_TENS_GEST', typ.StringType()),
    ('PREV_BIRTH_PRETERM', typ.StringType()),
    ('NO_RISK', typ.StringType()),
    ('NO_INFECTIONS_REPORTED', typ.StringType()),
    ('LABOR_IND', typ.StringType()),
    ('LABOR_AUGM', typ.StringType()),
    ('STEROIDS', typ.StringType()),
    ('ANTIBIOTICS', typ.StringType()),
    ('ANESTHESIA', typ.StringType()),
    ('DELIV_METHOD_RECODE_COMB', typ.StringType()),
    ('ATTENDANT_BIRTH', typ.StringType()),
    ('APGAR_5', typ.IntegerType()),
    ('APGAR_5_RECODE', typ.StringType()),
    ('APGAR_10', typ.IntegerType()),
    ('APGAR_10_RECODE', typ.StringType()),
    ('INFANT_SEX', typ.StringType()),
    ('OBSTETRIC_GESTATION_WEEKS', typ.IntegerType()),
    ('INFANT_WEIGHT_GRAMS', typ.IntegerType()),
    ('INFANT_ASSIST_VENTI', typ.StringType()),
    ('INFANT_ASSIST_VENTI_6HRS', typ.StringType()),
    ('INFANT_NICU_ADMISSION', typ.StringType()),
    ('INFANT_SURFACANT', typ.StringType()),
    ('INFANT_ANTIBIOTICS', typ.StringType()),
    ('INFANT_SEIZURES', typ.StringType()),
    ('INFANT_NO_ABNORMALITIES', typ.StringType()),
    ('INFANT_ANCEPHALY', typ.StringType()),
    ('INFANT_MENINGOMYELOCELE', typ.StringType()),
    ('INFANT_LIMB_REDUCTION', typ.StringType()),
    ('INFANT_DOWN_SYNDROME', typ.StringType()),
    ('INFANT_SUSPECTED_CHROMOSOMAL_DISORDER', typ.StringType()),
    ('INFANT_NO_CONGENITAL_ANOMALIES_CHECKED', typ.StringType()),
    ('INFANT_BREASTFED', typ.StringType())
]

schema = typ.StructType([
    typ.StructField(e[0], e[1], False) for e in labels
])

# spark = SparkSession.builder.config('spark.debug.maxToStringFields', '100').config('spark.io.compression.codec', 'snappy').appName("test").getOrCreate();
# births = spark.read.csv(datafile,header=True,schema=schema,encoding='ISO-8859-1')  #绑定的schema

spark = SparkSession.builder.config('spark.debug.maxToStringFields', '100').config('spark.io.compression.codec',
                                                                                   'snappy').appName(
    "test").getOrCreate()

# 读取方法
# births=spark.read.format("csv").\
#     option("header","true")\
#     .load("births_train.csv")


births = spark.read.csv(datafile, header=True, schema=schema)

'''
婴儿的生存情况，关注父母的信息
'''

selected_features = [
    'INFANT_ALIVE_AT_REPORT',
    'BIRTH_PLACE',
    'MOTHER_AGE_YEARS',
    'FATHER_COMBINED_AGE',
    'CIG_BEFORE',
    'CIG_1_TRI',
    'CIG_2_TRI',
    'CIG_3_TRI',
    'MOTHER_HEIGHT_IN',
    'MOTHER_PRE_WEIGHT',
    'MOTHER_DELIVERY_WEIGHT',
    'MOTHER_WEIGHT_GAIN',
    'DIABETES_PRE',
    'DIABETES_GEST',
    'HYP_TENS_PRE',
    'HYP_TENS_GEST',
    'PREV_BIRTH_PRETERM'
]

births_trimmed = births.select(selected_features)

'''
对于孕期吸烟量的处理
0：不吸烟
1-98：实际数量
99：未知
把未知当做不吸烟来处理
'''
import pyspark.sql.functions as func


def correct_cig(feat):
    return func \
        .when(func.col(feat) != 99, func.col(feat)) \
        .otherwise(0)


'''
withColumn：第一个参数列名，第二个参数：函数
'''
births_transformed = births_trimmed \
    .withColumn('CIG_BEFORE', correct_cig('CIG_BEFORE')) \
    .withColumn('CIG_1_TRI', correct_cig('CIG_1_TRI')) \
    .withColumn('CIG_2_TRI', correct_cig('CIG_2_TRI')) \
    .withColumn('CIG_3_TRI', correct_cig('CIG_3_TRI'))

# print births_transformed.take(2)

'''
筛选所有值为Y|N|U编码的列   模型训练只能是数字整形
'''
cols = [(col.name, col.dataType) for col in births_trimmed.schema]

'''
结果
cols
[('INFANT_ALIVE_AT_REPORT', StringType), ('BIRTH_PLACE', StringType), ('MOTHER_AGE_YEARS', IntegerType), ('FATHER_COMBINED_AGE', IntegerType), ('CIG_BEFORE', IntegerType), ('CIG_1_TRI', IntegerType), ('CIG_2_TRI', IntegerType), ('CIG_3_TRI', IntegerType), ('MOTHER_HEIGHT_IN', IntegerType), ('MOTHER_PRE_WEIGHT', IntegerType), ('MOTHER_DELIVERY_WEIGHT', IntegerType), ('MOTHER_WEIGHT_GAIN', IntegerType), ('DIABETES_PRE', StringType), ('DIABETES_GEST', StringType), ('HYP_TENS_PRE', StringType), ('HYP_TENS_GEST', StringType), ('PREV_BIRTH_PRETERM', StringType)]
['INFANT_ALIVE_AT_REPORT', 'BIRTH_PLACE', 'MOTHER_AGE_YEARS', 'FATHER_COMBINED_AGE', 'CIG_BEFORE', 'CIG_1_TRI', 'CIG_2_TRI', 'CIG_3_TRI', 'MOTHER_HEIGHT_IN', 'MOTHER_PRE_WEIGHT', 'MOTHER_DELIVERY_WEIGHT', 'MOTHER_WEIGHT_GAIN', 'DIABETES_PRE', 'DIABETES_GEST', 'HYP_TENS_PRE', 'HYP_TENS_GEST', 'PREV_BIRTH_PRETERM']
'''
YNU_cols = ['INFANT_ALIVE_AT_REPORT', 'DIABETES_PRE', 'DIABETES_GEST', 'HYP_TENS_PRE', 'HYP_TENS_GEST',
            'PREV_BIRTH_PRETERM']

'''
births.select('INFANT_ALIVE_AT_REPORT').distinct().show()
结果是
+----------------------+
|INFANT_ALIVE_AT_REPORT|
+----------------------+
|                     Y|
|                     N|
+----------------------+

print births.select('INFANT_ALIVE_AT_REPORT').distinct().rdd.map(lambda row:row[0]).collect()   

结果
[u'Y', u'N']
print births.select('INFANT_ALIVE_AT_REPORT').distinct().rdd.map(lambda row:len(row)).collect()
[1, 1]

dis = [u'Y', u'N']
'''

# 查询所以列包括Y的字段，把带Y的字段放到列表进而

# s[1] 是类型 s[0]是字段名称
# for i, s in enumerate(cols):
#     if s[1] == typ.StringType():
#         dis = births.select(s[0]) \
#             .distinct() \
#             .rdd \
#             .map(lambda row: row[0]) \
#             .collect()
#         if 'Y' in dis:
#             YNU_cols.append(s[0])
# print '----------------------------'
# print YNU_cols
'''
对于要预测的目标变量重新编码，封装成udf，返回类型integer
'''
'''
udf:把用户方法封装成一个可以在DataFrame中使用的方法，参数1：用户方法，参数2：返回值类型
这个用户方法的第一个参数一定是一个Column类型，是有sparksql自动传入的
'''

recode_dictionary = {
    'YNU': {
        'N': 1,
        'Y': 0,
        'U': 0
    }
}


# 取字典值的方法recode_dictionary['YNU']['Y']
# key 是YNU
def recode(col, key):
    return recode_dictionary[key][col]


rec_integer = func.udf(recode, typ.IntegerType())  # 第一个udf函数，第二个是返回的类型
# print rec_integer('INFANT_ALIVE_AT_REPORT',func.lit('YNU')).alias('INFANT_ALIVE_AT_REPORT')
# 结果Column<recode(INFANT_ALIVE_AT_REPORT, YNU) AS `INFANT_ALIVE_AT_REPORT`>

# print func.lit('YNU')
# 结果Column<YNU>


exprs_YNU = [
    rec_integer(x, func.lit('YNU')).alias(x)  # x
    if x in YNU_cols
    else x
    for x in births_transformed.columns
]
# recode(INFANT_ALIVE_AT_REPORT, YNU)  INFANT_ALIVE_AT_REPOR返回的值是（Y,N,U） 对应每列取出相应的值 1 0 0

'''
结果
[Column<recode(INFANT_ALIVE_AT_REPORT, YNU) AS `INFANT_ALIVE_AT_REPORT`>, 'BIRTH
_PLACE', 'MOTHER_AGE_YEARS', 'FATHER_COMBINED_AGE', 'CIG_BEFORE', 'CIG_1_TRI', '
CIG_2_TRI', 'CIG_3_TRI', 'MOTHER_HEIGHT_IN', 'MOTHER_PRE_WEIGHT', 'MOTHER_DELIVE
RY_WEIGHT', 'MOTHER_WEIGHT_GAIN', Column<recode(DIABETES_PRE, YNU) AS `DIABETES_
PRE`>, Column<recode(DIABETES_GEST, YNU) AS `DIABETES_GEST`>, Column<recode(HYP_
TENS_PRE, YNU) AS `HYP_TENS_PRE`>, Column<recode(HYP_TENS_GEST, YNU) AS `HYP_TEN
S_GEST`>, Column<recode(PREV_BIRTH_PRETERM, YNU) AS `PREV_BIRTH_PRETERM`>]
'''

'''
最后的干净的数据集
'''
births_transformed = births_transformed.select(exprs_YNU)

# ===================== phase 2 ：了解数据，描述统计========================================
import pyspark.mllib.stat as st
import numpy as np

# 获得数值型变量的统计信息，包括均值和方差等
numeric_cols = ['MOTHER_AGE_YEARS', 'FATHER_COMBINED_AGE',
                'CIG_BEFORE', 'CIG_1_TRI', 'CIG_2_TRI', 'CIG_3_TRI',
                'MOTHER_HEIGHT_IN', 'MOTHER_PRE_WEIGHT',
                'MOTHER_DELIVERY_WEIGHT', 'MOTHER_WEIGHT_GAIN'
                ]
'''
births_transformed.select(numeric_cols).show(10)
结果
+----------------+-------------------+----------+---------+---------+---------+----------------+-----------------+----------------------+------------------+
|MOTHER_AGE_YEARS|FATHER_COMBINED_AGE|CIG_BEFORE|CIG_1_TRI|CIG_2_TRI|CIG_3_TRI|MOTHER_HEIGHT_IN|MOTHER_PRE_WEIGHT|MOTHER_DELIVERY_WEIGHT|MOTHER_WEIGHT_GAIN|
+----------------+-------------------+----------+---------+---------+---------+----------------+-----------------+----------------------+------------------+
|              29|                 99|         0|        0|        0|        0|              99|              999|                   999|                99|
|              22|                 29|         0|        0|        0|        0|              65|              180|                   198|                18|
|              38|                 40|         0|        0|        0|        0|              63|              155|                   167|                12|
|              39|                 42|         0|        0|        0|        0|              60|              128|                   152|                24|
'''

numeric_rdd = births_transformed \
    .select(numeric_cols) \
    .rdd \
    .map(lambda row: [e for e in row])

# 把每一行的数据转换成一个list，转成向量，以便进行学习，
# [29, 99, 0, 0, 0, 0, 99, 999, 999, 99], [22, 29, 0, 0, 0, 0, 65, 180, 198, 18], [38, 40, 0, 0, 0, 0, 63, 155, 167, 12]


# colStats:以列为基础计算统计量的基本数据
mllib_stats = st.Statistics.colStats(numeric_rdd)

# count、max、mean、min、normL1、normL2、numNonzeros、variance

# for col,m,v in zip(numeric_cols,
#                    mllib_stats.mean(),
#                    mllib_stats.variance()):   #方差
#     print('{0}: \t{1:.2f} \t {2:.2f}'.format(col, m, np.sqrt(v)))  #sqrt  根据方差计算平方根

'''  计算没一列的平均值和方差
MOTHER_AGE_YEARS:       28.30    6.08
FATHER_COMBINED_AGE:    44.55    27.55
CIG_BEFORE:     1.43     5.18
CIG_1_TRI:      0.91     3.83
CIG_2_TRI:      0.70     3.31
CIG_3_TRI:      0.58     3.11
MOTHER_HEIGHT_IN:       65.12    6.45
MOTHER_PRE_WEIGHT:      214.50   210.21
MOTHER_DELIVERY_WEIGHT:         223.63   180.01
MOTHER_WEIGHT_GAIN:     30.74    26.23
'''

# 类别变量， 计算频数,不在上面统计中的列

# categorical_cols = [e for e in births_transformed.columns
#                     if e not in numeric_cols]
# 结果['INFANT_ALIVE_AT_REPORT', 'BIRTH_PLACE', 'DIABETES_PRE', 'DIABETES_GEST', 'HYP_TENS_PRE', 'HYP_TENS_GEST', 'PREV_BIRTH_PRETERM']
# print categorical_cols
# 上面算过后，把结果直接写在下面，以便测试会快点，
categorical_cols = ['INFANT_ALIVE_AT_REPORT', 'BIRTH_PLACE', 'DIABETES_PRE', 'DIABETES_GEST', 'HYP_TENS_PRE',
                    'HYP_TENS_GEST', 'PREV_BIRTH_PRETERM']

categorical_rdd = births_transformed \
    .select(categorical_cols) \
    .rdd \
    .map(lambda row: [e for e in row])
'''
结束：也是把列转换为数组List
[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1],
'''
# print categorical_rdd.collect()
# 结果i= 0 1 2 3 4 5 6
# for i ,col in enumerate(categorical_cols):
#     agg = categorical_rdd \
#             .groupBy(lambda row:row[i]) \#根据列分组内容
#             .map(lambda  row:(row[0],len(row[1]))) #返回每列分组的数据和数量[(0, 23349), (1, 22080)])

# 看每列分组的数量
# for i ,col in enumerate(categorical_cols):
#     agg = categorical_rdd \
#         .groupBy(lambda row:row[i]) \
#         .map(lambda  row:(row[0],len(row[1])))
#     print(col,sorted(agg.collect(),
#                      key=lambda  e1:e1[1],  #根分组后总数从大到小进行排序
#                      reverse=True ))

'''结果
('INFANT_ALIVE_AT_REPORT', [(0, 23349), (1, 22080)])
('BIRTH_PLACE', [(1, 44558), (4, 327), (3, 224), (2, 136), (7, 91), (5, 74), (6, 11), (9, 8)])
('DIABETES_PRE', [(1, 44689), (0, 740)])
('DIABETES_GEST', [(1, 43259), (0, 2170)])
('HYP_TENS_PRE', [(1, 44156), (0, 1273)])
('HYP_TENS_GEST', [(1, 43110), (0, 2319)])
('PREV_BIRTH_PRETERM', [(1, 42896), (0, 2533)])
'''

# 计算相关系数矩阵

corrs = st.Statistics.corr(numeric_rdd)  # 得到相关系数据矩阵

# print corrs.take(20)
# 只挑选相关系数>0.5的这些特征
# for i ,el in enumerate(corrs>0.5):   #阵矩  横行
#     correlated = [
#         (numeric_cols[j],corrs[i][j])
#         for j,e in enumerate(el) if e==1.0 and j !=i]  #竖行
#     if len(correlated) > 0:
#         for e in correlated:
#             print('{0}-to-{1}: {2:.2f}' \
#                   .format(numeric_cols[i], e[0], e[1]))

'''
结果
CIG_BEFORE-to-CIG_1_TRI: 0.83
CIG_BEFORE-to-CIG_2_TRI: 0.72
CIG_BEFORE-to-CIG_3_TRI: 0.62
CIG_1_TRI-to-CIG_BEFORE: 0.83
CIG_1_TRI-to-CIG_2_TRI: 0.87
CIG_1_TRI-to-CIG_3_TRI: 0.76
CIG_2_TRI-to-CIG_BEFORE: 0.72
CIG_2_TRI-to-CIG_1_TRI: 0.87
CIG_2_TRI-to-CIG_3_TRI: 0.89
CIG_3_TRI-to-CIG_BEFORE: 0.62
CIG_3_TRI-to-CIG_1_TRI: 0.76
CIG_3_TRI-to-CIG_2_TRI: 0.89
MOTHER_PRE_WEIGHT-to-MOTHER_DELIVERY_WEIGHT: 0.54
MOTHER_PRE_WEIGHT-to-MOTHER_WEIGHT_GAIN: 0.65
MOTHER_DELIVERY_WEIGHT-to-MOTHER_PRE_WEIGHT: 0.54
MOTHER_DELIVERY_WEIGHT-to-MOTHER_WEIGHT_GAIN: 0.60
MOTHER_WEIGHT_GAIN-to-MOTHER_PRE_WEIGHT: 0.65
MOTHER_WEIGHT_GAIN-to-MOTHER_DELIVERY_WEIGHT: 0.60

'''

# 去掉相关性强的变量中的一个

features_to_keep = [
    'INFANT_ALIVE_AT_REPORT',
    'BIRTH_PLACE',
    'MOTHER_AGE_YEARS',
    'FATHER_COMBINED_AGE',
    'CIG_1_TRI',
    'MOTHER_HEIGHT_IN',
    'MOTHER_PRE_WEIGHT',
    'DIABETES_PRE',
    'DIABETES_GEST',
    'HYP_TENS_PRE',
    'HYP_TENS_GEST',
    'PREV_BIRTH_PRETERM'
]

births_transformed = births_transformed.select([e for e in features_to_keep])

# 对于类别型变量，不能直接计算相关系数判断相关性，但是可以用chi-square来检验相关性


# 对于类别型变量，不能直接计算相关系数判断相关性，但是可以用chi-square来检验相关性

import pyspark.mllib.linalg as ln

'''
BIRTH_PLACE
DIABETES_PRE
DIABETES_GEST
HYP_TENS_PRE
HYP_TENS_GEST
PREV_BIRTH_PRETERM
 agg=births_transformed \
        .groupby('INFANT_ALIVE_AT_REPORT') \
        .pivot("BIRTH_PLACE") \  #这个是出生地1，2，3，4，5，6，9离散的
        .count() 
[Row(INFANT_ALIVE_AT_REPORT=1, 1=21563, 2=23, 3=66, 4=288, 5=55, 6=9, 7=68, 9=8), Row(INFANT_ALIVE_AT_REPORT=0, 1=22995, 2=113, 3=158, 4=39, 5=19, 6=2, 7=23, 9=None)]
INFANT_ALIVE_AT_REPORT=1  #存活的每个出生地的数量 
INFANT_ALIVE_AT_REPORT=0    #死亡的每个出生地的数量

 下面INFANT_ALIVE_AT_REPORT列会与每一行对比生成类似与上面的数据，拿存活状况，与其它列进行比较，看下相关性和数量
'''

# for cat in categorical_cols[1:]:
#     agg=births_transformed \
#         .groupby('INFANT_ALIVE_AT_REPORT')\
#         .pivot(cat) \
#         .count()
#     #生成chi-square需要的格式
#     agg_rdd = agg \
#         .rdd \
#         .map(lambda row: (row[1:])) \
#         .flatMap(lambda row:[0 if e == None else e for e in row]) \
#         .collect()
#     ##例如取第一列row_lenght=8
#     row_length = len(agg.collect()[0])-1
#     ##例第一列，创建矩阵  长度为8，二维，数据 agg_rdd = [21563, 23, 66, 288, 55, 9, 68, 8, 22995, 113, 158, 39, 19, 2, 23, 0]
#     agg = ln.Matrices.dense(row_length, 2, agg_rdd)
#     ##得出关系 agg=[Row(INFANT_ALIVE_AT_REPORT=1, 1=21563, 2=23, 3=66, 4=288, 5=55, 6=9, 7=68, 9=8), Row(INFANT_ALIVE_AT_REPORT=0, 1=22995, 2=113, 3=158, 4=39, 5=19, 6=2, 7=23, 9=None)]
#     test = st.Statistics.chiSqTest(agg)
#     ##保留4位小数
#     print(cat, round(test.pValue, 4))


'''
print agg.collect()的结果
[Row(INFANT_ALIVE_AT_REPORT=1, 1=21563, 2=23, 3=66, 4=288, 5=55, 6=9, 7=68, 9=8), Row(INFANT_ALIVE_AT_REPORT=0, 1=22995, 2=113, 3=158, 4=39, 5=19, 6=2, 7=23, 9=None)]
[Row(INFANT_ALIVE_AT_REPORT=1, 0=539, 1=21541), Row(INFANT_ALIVE_AT_REPORT=0, 0=201, 1=23148)]
[Row(INFANT_ALIVE_AT_REPORT=1, 0=805, 1=21275), Row(INFANT_ALIVE_AT_REPORT=0, 0=1365, 1=21984)]
[Row(INFANT_ALIVE_AT_REPORT=1, 0=812, 1=21268), Row(INFANT_ALIVE_AT_REPORT=0, 0=461, 1=22888)]
[Row(INFANT_ALIVE_AT_REPORT=1, 0=1075, 1=21005), Row(INFANT_ALIVE_AT_REPORT=0, 0=1244, 1=22105)]
[Row(INFANT_ALIVE_AT_REPORT=1, 0=1839, 1=20241), Row(INFANT_ALIVE_AT_REPORT=0, 0=694, 1=22655)]
agg_rdd=agg \
        .rdd \
        .map(lambda row:(row[1:])) \
        .collect()
结果为：  取出里面的值
[(21563, 23, 66, 288, 55, 9, 68, 8), (22995, 113, 158, 39, 19, 2, 23, None)]
[(539, 21541), (201, 23148)]
[(805, 21275), (1365, 21984)]
[(812, 21268), (461, 22888)]

agg_rdd = agg \
        .rdd \
        .map(lambda row: (row[1:])) \
        .flatMap(lambda row:[0 if e == None else e for e in row]) \
        .collect()
        结果：
[21563, 23, 66, 288, 55, 9, 68, 8, 22995, 113, 158, 39, 19, 2, 23, 0]
[539, 21541, 201, 23148]   

 row_length = len(agg.collect()[0])-1
    print agg.collect()[0]   结果  Row(INFANT_ALIVE_AT_REPORT=1, 1=21563, 2=23, 3=66, 4=288, 5=55, 6=9, 7=68, 9=8)
    print row_length  结果8，去掉INFANT_ALIVE_AT_REPORT=1
 Row(INFANT_ALIVE_AT_REPORT=1, 0=539, 1=21541)
 2
   print(cat, round(test.pValue, 4))


   结果  
BIRTH_PLACE 0.0
DIABETES_PRE 0.0
DIABETES_GEST 0.0  #pvalue的值，都是0，可以应为是独立的。没有相关性。
HYP_TENS_PRE 0.0
HYP_TENS_GEST 0.0
PREV_BIRTH_PRETERM 0.0
'''

import pyspark.mllib.feature as ft
import pyspark.mllib.regression as reg

hashing = ft.HashingTF(7)

'''
aa = births_transformed.rdd
print aa.take(1)  row[1])就是BIRTH_PLACE列
结果
[Row(INFANT_ALIVE_AT_REPORT=1, BIRTH_PLACE=1, MOTHER_AGE_YEARS=29, FATHER_COMBINED_AGE=99, CIG_1_TRI=0, MOTHER_HEIGHT_IN=99, MOTHER_PRE_WEIGHT=999, DIABETES_PRE=1, DIABETES_GEST=1, HYP_TENS_PRE=1, HYP_TENS_GEST=1, PREV_BIRTH_PRETERM=1)]
'''
# BIRTH_PLACE 要是字符串才行


births_hashed = births_transformed \
    .rdd \
    .map(lambda row: [
    list(hashing.transform(row[1]).toArray())
    if col == 'BIRTH_PLACE'
    else row[i]  # 一行一行的扫描  把第一行的所有字段扫描到，在下一行row[0],row[1]
    for i, col
    in enumerate(features_to_keep)]) \
    .map(lambda row: [[e] if type(e) == int else e
                      for e in row]) \
    .map(lambda row: [item for sublist in row
                      for item in sublist]) \
    .map(lambda row: reg.LabeledPoint(
    row[0],
    ln.Vectors.dense(row[1:]))
         )

'''
map1
births_hashed = births_transformed \
    .rdd \
    .map(lambda row: [
            list('1')
                if col == 'BIRTH_PLACE'
                else row[i]
            for i, col
            in enumerate(features_to_keep)])
结果
每一行
BIRTH_PLACE列替换成[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
[[1, [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 29, 99, 0, 99, 999, 1, 1, 1, 1, 1], [1, [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 22, 29, 0, 65, 180, 1, 1, 1, 1, 1]]
map2:
.map(lambda row: [[e] if type(e) == int else e
                      for e in row])
print births_hashed.take(2)   如果是int类型就单独组成一个list[]  [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0] 这个本来就是list类型就原格式输出
结果
    [
    [[0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [29], [99], [0], [99], [999], [0], [
0], [0], [0], [0]],
     [[0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [22], [29], [0],[65], [180], [0], [0], [0], [0], [0]]
     ]
map3,两个循环
    .map(lambda row: [item for sublist in row
                      for item in sublist]) \
结果
     [[0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 29, 99, 0, 99, 999, 0, 0, 0, 0, 0],
      [0,0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 22, 29, 0, 65, 180, 0, 0, 0, 0, 0]]
map 4
    .map(lambda row: reg.LabeledPoint(
            row[0],
            ln.Vectors.dense(row[1:]))
        )

 [LabeledPoint(0.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,29.0,99.0,0.0,99.0,999.0,0.0,0.0
,0.0,0.0,0.0]),
 LabeledPoint(0.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,22.0,29.0,0.0,65.0,180.0,0.0,0.0,0.0,0.0,0.0])]
第一个0.00是 NFANT_ALIVE_AT_REPORT=1这个字段存活状况
'''
'''
 拆分测试数据集、训练数据集
'''
births_train, births_test = births_hashed.randomSplit([0.6, 0.4])

'''训练模型好简单'''
from pyspark.mllib.classification import LogisticRegressionWithLBFGS

LR_Model = LogisticRegressionWithLBFGS.train(births_train, iterations=10)  # iterations迭代10次
# predict 评估
LR_results = (
    births_test.map(lambda row: row.label) \
        .zip(LR_Model \
             .predict(births_test \
                      .map(lambda row: row.features)))
).map(lambda row: (row[0], row[1] * 1.0))

'''评估模型效果'''

import pyspark.mllib.evaluation as ev

LR_evaluation = ev.BinaryClassificationMetrics(LR_results)
print('Area under PR: {0:.2f}'.format(LR_evaluation.areaUnderPR))
print('Area under ROC: {0:.2f}'.format(LR_evaluation.areaUnderROC))
LR_evaluation.unpersist()

'''
lambda  row:row.label  会列出所有存活状况列的数据
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, ]




lambda  row:row.features  后面特性的数据
[DenseVector([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 29.0, 99.0, 0.0, 99.0, 999.0, 1.0, 1.0, 1.0, 1.0, 1.0]), DenseVector([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 22.0, 29.0, 0.0, 65.0, 180.0, 1.0, 1.0, 1.0, 1.0, 1.0]), DenseVector([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 32.0, 37.0, 0.0, 66.0, 150.0, 1.0, 1.0, 1.0, 1.0, 1.0]), DenseVector([0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 25.0, 26.0, 0.0, 64.0, 136.0, 1.0, 1.0, 1.0, 1.0, 1.0]),

print births_test.collect()  结果
[LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,29.0,99.0,0.0,99.0,999.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,38.0,40.0,0.0,63.0,155.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,18.0,99.0,4.0,61.0,110.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,25.0,26.0,0.0,64.0,136.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,33.0,99.0,0.0,65.0,145.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,28.0,29.0,0.0,66.0,320.0,1.0,1.0,0.0,1.0,0.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,23.0,28.0,0.0,64.0,120.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,31.0,41.0,0.0,59.0,106.0,1.0,1.0,1.0,1.0,0.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,27.0,99.0,0.0,66.0,213.0,1.0,1.0,1.0,1.0,1.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,28.0,27.0,0.0,66.0,165.0,1.0,1.0,1.0,1.0,0.0]), LabeledPoint(1.0, [0.0,0.0,1.0,0.0,0.0,0.0,0.0,34.0,31.0,0.0,70.0,130.0,1.0,1.0,1.0,1.0,1.0])]


LR_Model.predict(births_test.map(lambda  row:row.features)).collect()  结果

[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 


LR_results =(
    births_test.map(lambda  row:row.label)\
    .zip(LR_Model \
         .predict(births_test\
                  .map(lambda  row:row.features))
         ))

print LR_results.take(10)
结果

[(1.0, 1), (1.0, 0), (1.0, 1), (1.0, 0), (1.0, 1), (1.0, 1), (1.0, 0), (1.0, 0), (1.0, 0), (1.0, 1)]


'''

'''
    使用随机森林
'''
from pyspark.mllib.tree import RandomForest

RF_model = RandomForest \
    .trainClassifier(data=births_train,
                     numClasses=2,
                     categoricalFeaturesInfo={},
                     numTrees=6,
                     featureSubsetStrategy='all',
                     seed=666)

RF_results = (
    births_test.map(lambda row: row.label) \
        .zip(RF_model \
             .predict(births_test \
                      .map(lambda row: row.features)))
)

RF_evaluation = ev.BinaryClassificationMetrics(RF_results)

print('Area under PR: {0:.2f}' \
      .format(RF_evaluation.areaUnderPR))
print('Area under ROC: {0:.2f}' \
      .format(RF_evaluation.areaUnderROC))
RF_evaluation.unpersist()

'''
Area under PR: 0.81
Area under ROC: 0.62
'''

# ======================phase 4 用卡方找重要特征后再训练 ==========================
selector = ft.ChiSqSelector(4).fit(births_train)

topFeatures_train = (
    births_train.map(lambda row: row.label) \
        .zip(selector \
             .transform(births_train \
                        .map(lambda row: row.features)))
).map(lambda row: reg.LabeledPoint(row[0], row[1]))

topFeatures_test = (
    births_test.map(lambda row: row.label) \
        .zip(selector \
             .transform(births_test \
                        .map(lambda row: row.features)))
).map(lambda row: reg.LabeledPoint(row[0], row[1]))

''' 再看LR '''

LR_Model_2 = LogisticRegressionWithLBFGS \
    .train(topFeatures_train, iterations=10)

LR_results_2 = (
    topFeatures_test.map(lambda row: row.label) \
        .zip(LR_Model_2 \
             .predict(topFeatures_test \
                      .map(lambda row: row.features)))
).map(lambda row: (row[0], row[1] * 1.0))

LR_evaluation_2 = ev.BinaryClassificationMetrics(LR_results_2)

print('Area under PR: {0:.2f}' \
      .format(LR_evaluation_2.areaUnderPR))
print('Area under ROC: {0:.2f}' \
      .format(LR_evaluation_2.areaUnderROC))
LR_evaluation_2.unpersist()

'''
Area under PR: 0.86
Area under ROC: 0.62
'''
