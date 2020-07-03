from kafka import KafkaConsumer

# train_station_traffic_statistics
# train_station_traffic

consumer = KafkaConsumer('train_station_traffic_statistics', bootstrap_servers=['192.168.110.150:9092','192.168.110.151:9092','192.168.110.152:9092'])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))