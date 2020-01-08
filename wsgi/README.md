Web服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

## Django:

对于Django，大而全的框架它的内部组件比较多，内部提供：ORM、Admin、中间件、Form、ModelForm、Session、缓存、信号、CSRF；功能也都挺完善的
```
pip install django
django-admin startproject myproject

python manage.py runserver 0.0.0.0:8088

django-admin startapp demo
```

## Flask :

flask，微型框架，内部组件就比较少了，但是有很多第三方组件来扩展它，比如说有那个wtform（与django的modelform类似，表单验证）、flask-sqlalchemy（操作数据库的）、flask-session、flask-migrate、flask-script、blinker可扩展强，第三方组件丰富。所以对他本身来说有那种短小精悍的感觉

## Tornado:

是一个轻量级的Web框架，异步非阻塞+内置WebSocket功能。

'目标'：通过一个线程处理N个并发请求(处理IO)。

内部组件：
  a.内部自己实现socket
  b.路由系统
  c.视图
  d.模板
  e.cookie
  f.csrf

## 共同点：

Django和Flask的共同点就是，他们2个框架都没有写socket，所以他们都是利用第三方模块wsgi;而Tornado自带socket组件。

## 不同点：

但是内部使用的wsgi也是有些不同的：Django本身运行起来使用wsgiref，而Flask使用werkzeug wsgi，还有一个区别就是他们的请求管理不太一样：django是通过将请求封装成request对象，再通过参数传递，而flask是通过上下文管理机制
