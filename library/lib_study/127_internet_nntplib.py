"""
网络新闻传输协议(NNTP，Network News Transfer Protocol)
NNTP用于向Internet上NNTP服务器或NNTP客户（新闻阅读器）发布网络新闻邮件的协议，
提供通过Internet使用可靠的基于流的新闻传输，提供新闻的分发、查询、检索和投递。
NNTP还专门设计用于将新闻文章保存在中心数据库的服务器上，这样用户可以选择要阅读的特定条目，还提供过期新闻的索引、交叉引用和终止。
"""
import nntplib

s = nntplib.NNTP('news.gmane.io')
resp, count, first, last, name = s.group('gmane.comp.python.committers')
print('Group', name, 'has', count, 'articles, range', first, 'to', last)

resp, overviews = s.over((last - 9, last))
for id, over in overviews:
    print(id, nntplib.decode_header(over['subject']))





s.quit()