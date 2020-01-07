import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)

"""
[Google 开源的 Python 命令行库：深入 fire（二）](https://mp.weixin.qq.com/s?__biz=MzA5MzYyNzQ0MQ==&mid=2247485006&idx=1&sn=d80725f349677658bff372bfc770e1de)

https://github.com/google/python-fire

python hello.py  # Hello World!
python hello.py --name=David  # Hello David!
python hello.py --help  # Shows usage information.
"""

