from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['192.168.110.150:9092','192.168.110.151:9092','192.168.110.152:9092'])

producer.send('kafka_sql_stream_topic', b'x.x,x x')

producer.close()