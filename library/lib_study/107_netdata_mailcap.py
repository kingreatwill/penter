# https://docs.python.org/zh-cn/3/library/mailcap.html
"""
Mailcap 文件可用来配置支持 MIME 的应用例如邮件阅读器和 Web 浏览器如何响应具有不同 MIME 类型的文件。
（"mailcap" 这个名称源自短语"mail capability"。） 例如，一个 mailcap 文件可能包含 video/mpeg; xmpeg %s 这样的行。
然后，如果用户遇到 MIME 类型为 video/mpeg 的邮件消息或 Web 文档时，%s 将被替换为一个文件名（通常是一个临时文件）并且将自动启动 xmpeg 程序来查看该文件。

mailcap 格式的文档见 RFC 1524, "A User Agent Configuration Mechanism For Multimedia Mail Format Information"，但它并不是一个因特网标准。
不过，mailcap 文件在大多数 Unix 系统上都受到支持。
"""

import mailcap
d = mailcap.getcaps()
print(mailcap.findmatch(d, 'video/mpeg', filename='tmp1223'))