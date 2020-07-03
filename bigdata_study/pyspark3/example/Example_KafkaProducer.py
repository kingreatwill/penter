import datetime
import random
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.110.150:9092','192.168.110.151:9092','192.168.110.152:9092'])

train_stations = ['深圳东站', '深圳南站', '深圳北站']

for i in range(10000):
    week1 = random.randint(10, 15)
    week2 = random.randint(20, 30)
    week3 = random.randint(30, 55)
    week4 = random.randint(50, 60)
    week5 = random.randint(60, 70)
    week6 = random.randint(70, 90)
    week7 = random.randint(80, 100)
    train_station = random.choice(train_stations)
    s = "{},{},{},{},{},{},{},{}".format(train_station, week1, week2, week3, week4, week5, week6, week7)
    print(s)
    producer.send('train_station_traffic', bytes(s, encoding="utf8"))
    time.sleep(1)

producer.flush()
producer.close()
print("ok")