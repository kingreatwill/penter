# https://docs.python.org/zh-cn/3.7/library/optparse.html#module-optparse

# u:python optparse_1.py -f hhh
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print(options)
print(args)