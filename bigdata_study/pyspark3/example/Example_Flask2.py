#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

from kafka import KafkaConsumer
consumer = KafkaConsumer('train_station_traffic_statistics',
                         bootstrap_servers=['192.168.110.150:9092', '192.168.110.151:9092', '192.168.110.152:9092'])
def background_thread():
    for msg in consumer:
        socketio.sleep(1)
        data_json = msg.value.decode('utf8')
        socketio.emit('send_message', {'data': data_json}, namespace='/test')



@app.route('/')
def index():
    return render_template('index2.html', async_mode=socketio.async_mode)


@socketio.on('connect', namespace='/test')
def teconnect():
    print("连接正常")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)



if __name__ == '__main__':
    socketio.run(app, debug=True)