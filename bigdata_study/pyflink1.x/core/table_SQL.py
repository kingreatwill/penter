from pyflink.table.types import DataTypes
if __name__ == '__main__':
    t = DataTypes.INTERVAL(DataTypes.DAY(), DataTypes.SECOND(3))
    # table = t_env.from_elements(
    #     [(1, 'ABC'), (2, 'ABCDE')],
    #     schema=DataTypes.ROW([DataTypes.FIELD('id', DataTypes.INT()),
    #                           DataTypes.FIELD('name', DataTypes.STRING())]))
    # )
# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/sql/queries.html
# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/sql/create.html#create-table
"""

CREATE TABLE user_actions (
  user_name STRING,
  data STRING,
  user_action_time TIMESTAMP(3),
  -- 声明user_action_time为事件时间属性，并使用5秒延迟水印策略 declare user_action_time as event time attribute and use 5 seconds delayed watermark strategy
  WATERMARK FOR user_action_time AS user_action_time - INTERVAL '5' SECOND
) WITH (
  ...
);

SELECT TUMBLE_START(user_action_time, INTERVAL '10' MINUTE), COUNT(DISTINCT user_name)
FROM user_actions
GROUP BY TUMBLE(user_action_time, INTERVAL '10' MINUTE);


CREATE TABLE user_actions (
  user_name STRING,
  data STRING,
  user_action_time AS PROCTIME() -- 声明一个额外的字段作为处理时间属性declare an additional field as a processing time attribute
) WITH (
  ...
);

SELECT TUMBLE_START(user_action_time, INTERVAL '10' MINUTE), COUNT(DISTINCT user_name)
FROM user_actions
GROUP BY TUMBLE(user_action_time, INTERVAL '10' MINUTE);

# Versioned Table
CREATE TABLE products (
	product_id    STRING,
	product_name  STRING,
	price         DECIMAL(32, 2),
	update_time   TIMESTAMP(3) METADATA FROM 'value.source.timestamp' VIRTUAL,
	PRIMARY KEY (product_id) NOT ENFORCED
	WATERMARK FOR update_time AS update_time
) WITH (...);

CREATE TABLE currency_rates (
	currency      STRING,
	rate          DECIMAL(32, 10)
	update_time   TIMESTAMP(3),
	WATERMARK FOR update_time AS update_time
) WITH (
	'connector' = 'kafka',
	'topic'	    = 'rates',
	'properties.bootstrap.servers' = 'localhost:9092',
	'format'    = 'json'
);

CREATE VIEW versioned_rates AS              
SELECT currency, rate, update_time              -- (1) `update_time` keeps the event time
  FROM (
      SELECT *,
      ROW_NUMBER() OVER (PARTITION BY currency  -- (2) the inferred unique key `currency` can be a primary key
         ORDER BY update_time DESC) AS rownum 
      FROM currency_rates)
WHERE rownum = 1; 
"""

"""
-- 如果两个输入表都是只追加的，那么资源使用可能会无限增长。
SELECT * FROM Orders
INNER JOIN Product
ON Orders.productId = Product.id

-- 根据时间关联
SELECT *
FROM
  Orders o,
  Shipments s
WHERE o.id = s.orderId AND
      o.ordertime BETWEEN s.shiptime - INTERVAL '4' HOUR AND s.shiptime
      
      
      
-- Create a table of orders. This is a standard
-- append-only dynamic table.
CREATE TABLE orders (
    order_id    STRING,
    price       DECIMAL(32,2),
    currency    STRING,
    order_time  TIMESTAMP(3),
    WATERMARK FOR order_time AS order_time
) WITH (...);

-- Define a versioned table of currency rates. 
-- This could be from a change-data-capture
-- such as Debezium, a compacted Kafka topic, or any other
-- way of defining a versioned table. 
CREATE TABLE currency_rates (
    currency STRING,
    conversion_rate DECIMAL(32, 2),
    update_time TIMESTAMP(3) METADATA FROM `values.source.timestamp` VIRTURAL
    WATERMARK FOR update_time AS update_time
) WITH (...);

-- Event Time
SELECT [column_list]
FROM table1 [AS <alias1>]
[LEFT] JOIN table2 FOR SYSTEM_TIME AS OF table1.{ proctime | rowtime } [AS <alias2>]
ON table1.column-name1 = table2.column-name1

SELECT 
     order_id,
     price,
     currency,
     conversion_rate,
     order_time,
FROM orders
LEFT JOIN currency_rates FOR SYSTEM_TIME AS OF orders.order_time
ON orders.currency = currency_rates.currency

-- Processing Time
SELECT
  o.amout, o.currency, r.rate, o.amount * r.rate
FROM
  Orders AS o
  JOIN LatestRates FOR SYSTEM_TIME AS OF o.proctime AS r
  ON r.currency = o.currency
"""
# TOP-N SQL https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/sql/queries.html#top-n
""" 
SELECT [column_list]
FROM (
   SELECT [column_list],
     ROW_NUMBER() OVER ([PARTITION BY col1[, col2...]]
       ORDER BY col1 [asc|desc][, col2 [asc|desc]...]) AS rownum
   FROM table_name)
WHERE rownum <= N [AND conditions]
"""
# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/table/sql/queries.html#selecting-group-window-start-and-end-timestamps
"""
计算每天的总和(金额)(以事件时间计算)
SELECT user,  TUMBLE_START(rowtime, INTERVAL '1' DAY) as wStart,  SUM(amount) FROM Orders  GROUP BY TUMBLE(rowtime, INTERVAL '1' DAY), user

每天合计(数量)(以处理时间计算)
SELECT user, SUM(amount) FROM Orders GROUP BY TUMBLE(proctime, INTERVAL '1' DAY), user

每小时计算事件时间中过去24小时的总和(数量)
SELECT product, SUM(amount) FROM Orders GROUP BY HOP(rowtime, INTERVAL '1' HOUR, INTERVAL '1' DAY), product

计算每个有12小时未活动间隔的会话的总和(以事件时间计算)
SELECT user,  SESSION_START(rowtime, INTERVAL '12' HOUR) AS sStart,  SESSION_ROWTIME(rowtime, INTERVAL '12' HOUR) AS snd, SUM(amount) FROM Orders GROUP BY SESSION(rowtime, INTERVAL '12' HOUR), user
"""