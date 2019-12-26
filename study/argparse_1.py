import argparse
# https://docs.python.org/zh-cn/3.7/library/argparse.html#module-argparse
# u:python argparse_1.py -o hhh
## 文件名不能和包名argparse相同argparse.py
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    print(args.output)
    # ... do something with args.output ...
    # ... do something with args.verbose ..