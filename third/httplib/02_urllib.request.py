import urllib.request

res = urllib.request.urlopen("http://httpbin.org/get")
print(res.read().decode("utf-8"))  # 自己解码