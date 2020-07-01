
"""

//按limit分页
    val partitons= new Array[String](3);
    partitons(0)="1=1 limit 0,10000";
    partitons(1)="1=1 limit 10000,10000";
    partitons(2)="1=1 limit 20000,10000";

session.read.jdbc(prop.getProperty("url"), prop.getProperty("dbtable"), partitons,prop)


这种方式就是通过指定数据库中某个字段的范围
val lowerBound = 1
val upperBound = 100000
val numPartitions = 5
val url = "jdbc:mysql://www.iteblog.com:3306/iteblog?user=iteblog&password=iteblog"

val prop = new Properties()
val df = sqlContext.read.jdbc(url, "iteblog", "id", lowerBound, upperBound, numPartitions, prop)

根据任意字段进行分区
val predicates = Array[String]("reportDate <= '2014-12-31'",
    "reportDate > '2014-12-31' and reportDate <= '2015-12-31'")
val url = "jdbc:mysql://www.iteblog.com:3306/iteblog?user=iteblog&password=iteblog"

val prop = new Properties()
val df = sqlContext.read.jdbc(url, "iteblog", predicates, prop)
"""
#  Spark读取Mysql大表(超百万/千万数据量的表) http://www.luyixian.cn/news_show_330053.aspx
# 直接从MySQL中Select大量数据，对MySQL的影响非常大，容易造成慢查询，影响业务线上的正常服务。
# Sqoop将MySQL的表数据同步到Hive
"""
package utils

import java.sql.{Connection, DriverManager}
import java.util.Properties
import org.apache.spark.sql.{DataFrame, SaveMode}

object ConnectUtils {

  private val properties: Properties = PropertiesUtils.getProperties

  /**
   * mysql数据源输入
   */
  def mysqlSource: (String) =>
    DataFrame = (tableName: String) => {
    val prop = new Properties()
    prop.setProperty("user", properties.getProperty("mysql.user"))
    prop.setProperty("password", properties.getProperty("mysql.password"))
    prop.setProperty("driver", "com.mysql.jdbc.Driver")

    //是否开启读大表配置
    if (properties.getProperty("mysql.isPartition").equals("true")) {
      //表数据大小
      val tableCount: Int = properties.getProperty("mysql.tableCount").toInt
      //每页数据大小
      val partitionLimit: Int = properties.getProperty("mysql.partitionLimit").toInt
      //需要的分页数
      val pages: Int = tableCount / partitionLimit
      //分页条件
      val partitionArray = new Array[String](pages)
      val orderField: String = properties.getProperty("mysql.orderField")
      for (i <- 0 until pages) {
        //        partitionArray(i) = s"1=1 order by ${properties.getProperty("mysql.orderField")} limit ${i * partitionLimit},${partitionLimit}"
        // 考虑到mysql在超大数据量查询时limit的性能问题，建议用这种方式进行limit分页
        partitionArray(i) = s"1=1 and ${orderField} >=(select ${orderField} from ${tableName} order by ${orderField} limit ${i * partitionLimit},1) limit ${partitionLimit}"
      }
      SparkUtils.sparkSessionWithHive.read.jdbc(properties.getProperty("mysql.url"), tableName, partitionArray, prop)
    } else {
      SparkUtils.sparkSessionWithHive.read.jdbc(properties.getProperty("mysql.url"), tableName, prop)
    }
  }
  
}
"""
# Mysql to Hive
"""
package demo

import org.apache.spark.sql.{DataFrame, SaveMode, SparkSession}
import utils.{ConnectUtils, SparkUtils}

object MysqlToHive {
  def main(args: Array[String]): Unit = {
    //创建session
    val spark: SparkSession = SparkUtils.sparkSessionWithHive

    //连接mysql
    //TODO 修改表名
    val dataDF: DataFrame = ConnectUtils.mysqlSource("table_test01")
    dataDF.show()

    //TODO 具体业务逻辑处理
    //通过调用API的方式保存到hive
//    dataDF.write.mode(SaveMode.Append).insertInto("databases_test..table_test01")

    //方式二：利用API自动创建表再插入数据
    //dataDF.write.mode(SaveMode.Append).saveAsTable("test_xsh_0401")
    //方式三：利用SQL插入已存在的表
    //    dataDF.createTempView("qiaoJie")
    //    sql("insert into table ods_xsh_0330 select * from qiaoJie")

    println("OK。。。。。")

    //释放资源
    spark.stop()
  }
}
"""