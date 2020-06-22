
# spark-submit --packages graphframes:graphframes:0.8.0-spark2.4-s_2.11 pygraphx.py


from pyspark import SparkContext
from pyspark.sql import SQLContext
from graphframes import *

# https://db-engines.com/en/ranking/graph+dbms
# 在图计算中，基本的数据结构表达就是：
# G = （V，E，D） V = vertex （顶点或者节点） E = edge （边） D = data （权重）
if __name__ == "__main__":
  sc = SparkContext(appName='graphframes')
  sqlContext = SQLContext(sc)

  # Vertex 顶点 DataFrame
  v = sqlContext.createDataFrame([
    ("a", "Alice", 34),
    ("b", "Bob", 36),
    ("c", "Charlie", 30),
    ("d", "David", 29),
    ("e", "Esther", 32),
    ("f", "Fanny", 36),
    ("g", "Gabby", 60)
  ], ["id", "name", "age"])
  # Edge 边 DataFrame
  e = sqlContext.createDataFrame([
    ("a", "b", "friend"),
    ("b", "c", "follow"),
    ("c", "b", "follow"),
    ("f", "c", "follow"),
    ("e", "f", "follow"),
    ("e", "d", "friend"),
    ("d", "a", "friend"),
    ("a", "e", "friend")
  ], ["src", "dst", "relationship"])

  # Create a GraphFrame
  g = GraphFrame(v, e)

  g.inDegrees.show()

  g.outDegrees.show()

  g.vertices.groupBy().min("age").show()

  c = g.edges.filter("relationship = 'follow'").count()
  print("relationship = 'follow' Count: "+str(c))

  # 图案的基本单位是边。例如，“(a)-[e]->(b)”表示从顶点a到顶点b的边e。注意，顶点用括号(a)表示，边用方括号[e]表示。
  motifs = g.find("(a)-[e]->(b); (b)-[e2]->(a)")
  motifs.show()

  motifs.filter("b.age > 30").show()

  g.find("(a)-[ab]->(b); (b)-[bc]->(c); (c)-[cd]->(d)").show()

  # PageRank算法.
  results = g.pageRank(resetProbability=0.15, maxIter=1)
  print(results)
  results.vertices.select("id", "pagerank").show()