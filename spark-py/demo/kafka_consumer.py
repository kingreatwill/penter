from kafka import KafkaConsumer
# latest 表示消费最新消息,earliest 表示从头开始消费,默认latest
consumer = KafkaConsumer('kafka_sql_stream_topic',group_id="demo_001_test2",auto_offset_reset='earliest',
                         bootstrap_servers=['192.168.110.150:9092','192.168.110.151:9092','192.168.110.152:9092'])
for msg in consumer:
    print (msg)