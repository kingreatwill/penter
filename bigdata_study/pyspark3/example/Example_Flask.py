import json
from threading import Lock

from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

consumer = KafkaConsumer('train_station_traffic_statistics',
                         bootstrap_servers=['192.168.110.150:9092', '192.168.110.151:9092', '192.168.110.152:9092'])


# 接收到消息就调用send_message方法，send_message是定义在web_socket对象上的js函数
def background_thread():
    for msg in consumer:
        socketio.sleep(1)
        data_json = msg.value.decode('utf8')
        socketio.emit('send_message', {'data': data_json}, namespace='/test')


# JS代码中可以调用这个装饰器下的视图函数，以初始化消费者监听kafka
@socketio.on('test_connect', namespace='/test')
def connect(message):
    print(message)
    socketio.emit('connected', {'data': 'Connected'}, namespace='/test')



@socketio.on('connect', namespace='/test')
def teconnect():
    print("连接正常")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

# 返回一个html页面
@app.route("/")
def handle_mes():
    return render_template("index.html", async_mode=socketio.async_mode)


"""
flask 默认的 前端路径再 templates下，静态文件再 static下
如果不移动或者修改 app默认路径，可以直接这样写：
app = Flask(__name__)

如果有修改，可以这样写：
app = Flask(__name__,template_folder='../xxxx',static_folder="../xxxx")
#template_folder='../xxxx' 指 前端文件的目录
#static_folder="../xxxx"  指 静态文件的目录
"""
# http://127.0.0.1:5000/
if __name__ == '__main__':
    socketio.run(app, debug=True)
