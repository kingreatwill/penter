import logging
import time

l = logging.Logger("name",level=logging.DEBUG)
print(l.getEffectiveLevel())
print(l.isEnabledFor(logging.INFO))
l.setLevel(logging.INFO)# 没有用？？
l.debug("debug")
l.info("info")
l.error("error")

#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(format='%(asctime)-15s %(clientip)s %(user)-8s %(message)s')
"""
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息
"""
log = logging.getLogger("name")
log.setLevel(logging.DEBUG)# 没有用？？
#log.warning('Protocol problem: %s', 'connection reset', extra={'clientip': '192.168.0.1', 'user': 'fbloggs'})
log.debug("debug")
log.info("info")
log.error("error")
