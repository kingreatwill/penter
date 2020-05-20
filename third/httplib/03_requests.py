import requests
# https://www.cnblogs.com/superhin/p/11455240.html
res = requests.get("http://httpbin.org/get")
print(res.text) # 自动按默认utf-8解码

# Post x-www-form-urlencoded传统表单请求
data = {"name":"张三", "age": 12}
res = requests.post("http://httpbin.org/post", data=data) # 自动编码
print(res.text)

# Post application/json请求
data = {"name":"张三", "age": 12}
res = requests.post("http://httpbin.org/post", json=data)
print(res.json())  # 转为字典格式

import json
# Post application/json请求
data = {"name":"张三", "age": 12}
headers = {"Content-Type": "application/json"}
res = requests.post("http://httpbin.org/post", data=json.dumps(data), headers=headers)
print(res.json())  # 转为字典格式