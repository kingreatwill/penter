import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt") # 设置指向 robots.txt 文件的 URL。
rp.read() # 读取 robots.txt URL 并将其输入解析器。

rrate = rp.request_rate("*")
# 以 named tuple RequestRate(requests, seconds) 的形式从 robots.txt 返回 Request-rate 形参的内容。
# 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。


print(rrate.requests)  # 3

print(rrate.seconds)  # 20


# 为指定的 useragent 从 robots.txt 返回 Crawl-delay 形参。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。
print(rp.crawl_delay("*"))  # 6


# 如果允许 useragent 按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。
print(rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))  # False

print(rp.can_fetch("*", "http://www.musi-cal.com/"))  # True
