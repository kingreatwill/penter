# 最新的，master（开发中）
https://ci.apache.org/projects/flink/flink-docs-master/api/python/

Flink 提供的两个核心API就是DataSet APl和DataStream APl。你没看错，名字和Spark的DataSet（python中没有）、DataFrame 非常相似。
顾名思义，DataSet代表有界的数据集，而DataStream代表流数据。所以，DataSet API是用来做批处理的，而DataStream API是做流处理的。
也许你会问，Flink 这样基于流的模型是怎样支持批处理的？在内部，DataSet 其实也用Stream表示，静态的有界数据也可以被看作是特殊的流数据，而且DataSet与DataStream 可以无缝切换。
所以，Flink的核心是DataStream。

DataStream API
DataSet API
Table API & SQL


# Stateful Functions Documentation
https://ci.apache.org/projects/flink/flink-statefun-docs-master/
有状态功能是一个开源框架，可降低大规模构建和协调分布式有状态应用程序的复杂性。 它将流处理的优点与ApacheFlink®和功能即服务（FaaS）结合在一起，为下一代事件驱动的体系结构提供了强大的抽象。

https://flink.apache.org/news/2020/04/07/release-statefun-2.0.0.html#event-driven-database-vs-requestresponse-database

2020-4-7, Apache Flink 团队，宣布了Stateful Functions (StateFun) 2.0正式发布--Stateful Functions第一次作为Apache Flink项目一部分的发布。
这是个巨大的里程碑: Stateful Functions 2.0不仅仅是一个API升级，而是基于第一版基于Apache Flink之上构建的事件驱动数据库(event-driven database)。

Stateful Functions 2.0 使有状态性和弹性有效的结合在一起，实现了类似AWS Lambada和Kubernetes资源编排工具的快速缩放/缩放到零以及滚动升级的特性。

通过这些特性， Stateful Functions 2.0有效的解决了FaaS被诟病的两个缺点：状态一致性和函数间消息交换效率。

# Flink Python 教材
https://ci.apache.org/projects/flink/flink-docs-release-1.12/zh/dev/python/table-api-users-guide/intro_to_table_api.html