import http.client

# h1 = http.client.HTTPConnection('www.python.org')
# h2 = http.client.HTTPConnection('www.python.org:80')
# h3 = http.client.HTTPConnection('www.python.org', 80)
# h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)


# 要通过一个运行于本机 8080 端口的 HTTPS 代理服务器隧道，我们应当向 HTTPSConnection 构造器传入代理的地址，并将我们最终想要访问的主机地址传给 set_tunnel() 方法:
# conn = http.client.HTTPSConnection("localhost", 8080)
# conn.set_tunnel("www.python.org")
# conn.request("HEAD","/index.html")

conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
# conn.request("POST", "", params, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()  # This will return entire content.
print(data1)


print("----------------------------------------------")
# The following example demonstrates reading data in chunks.
conn.request("GET", "/")
r1 = conn.getresponse()

chunk = r1.read(200)
while chunk != b"":
    print(repr(chunk))
    chunk = r1.read(200)

# Example of an invalid request
conn = http.client.HTTPSConnection("docs.python.org")
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)

data2 = r2.read()
print(data2)
conn.close()


"""
import http.client, urllib.parse
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = http.client.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
data

conn.close()

import http.client
BODY = "***filecontents***"
conn = http.client.HTTPConnection("localhost", 8080)
conn.request("PUT", "/file", BODY)
response = conn.getresponse()
print(response.status, response.reason)
"""