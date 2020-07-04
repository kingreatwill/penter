https://github.com/aaugustin/websockets

https://github.com/stephenmcd/django-socketio

https://github.com/miguelgrinberg/Flask-SocketIO
https://github.com/heroku-python/flask-sockets

[Flask-socketio多workers实现](https://www.jianshu.com/p/3c3e18456ccc)
# socketio=SocketIO(app,message_queue='redis://') # 'redis://localhost:6379/'    'amqp://guest:guest@localhost:5672//'  'kafka://'
https://flask-socketio.readthedocs.io/en/latest/
https://docs.celeryproject.org/projects/kombu/en/latest/userguide/connections.html?highlight=urls#urls
```
if url:
    if url.startswith(('redis://', "rediss://")):
        queue_class = socketio.RedisManager
    elif url.startswith(('kafka://')):
        queue_class = socketio.KafkaManager
    elif url.startswith('zmq'):
        queue_class = socketio.ZmqManager
    else:
        queue_class = socketio.KombuManager
    queue = queue_class(url, channel=channel,
                        write_only=write_only)
    self.server_options['client_manager'] = queue
```
