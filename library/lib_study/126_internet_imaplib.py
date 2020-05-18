import getpass, imaplib
# IMAP4(Internet Message Access Protocol 4) 即 交互式数据消息访问协议第四个版本
"""
与POP3协议类似，IMAP（Internet消息访问协议）也是提供面向用户的邮件收取服务。常用的版本是IMAP4。IMAP4改进了POP3的不足，
用户可以通过浏览信件头来决定是否收取、删除和检索邮件的特定部分，还可以在服务器上创建或更改文件夹或邮箱，
它除了支持POP3协议的脱机操作模式外，还支持联机操作和断连接操作。它为用户提供了有选择的从邮件服务器接收邮件的功能、基于服务器的信息处理功能和共享信箱功能。
IMAP4的脱机模式不同于POP3，它不会自动删除在邮件服务器上已取出的邮件，其联机模式和断连接模式也是将邮件服务器作为“远程文件服务器”进行访问，更加灵活方便。

pop3和imap4的最大区别是：使用pop协议，把服务器上的邮件下载到本地抄来处理，任何处理都在本地；是imap4协议，本地的处理实际上是与服务器交互后，在服务器上处理。

POP的全称是 Post Office Protocol，即邮局协议，用于电子邮件袭的接收，它使用TCP的110端口；POP是因特网知电子邮件的第一个离线协议标准,
POP3允许用户从服务器上把邮件存储到本地主机（道即自己的计算机）上,同时删除保存在邮件服务器上的邮件。

IMAP（Internet Mail Access Protocol，Internet邮件访问协议）以前称作交互邮件访问协议（Interactive Mail Access Protocol），
主要作用是邮件客户端（例如MS Outlook Express)可以通过这种协议从邮件服务器上获取邮件的信息，下载邮件等，使用的端口是143。
"""
M = imaplib.IMAP4("domain.org")
M.login(getpass.getuser(), getpass.getpass())
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()