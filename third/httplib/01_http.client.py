import http.client

# 1. 建立HTTP连接
conn = http.client.HTTPConnection("httpbin.org")
# 2. 发送GET请求，制定接口路径
conn.request("GET", '/get')
# 3. 获取相应
res = conn.getresponse()
# 4. 解析相应.进行解码
print(res.read()) # 自己解码