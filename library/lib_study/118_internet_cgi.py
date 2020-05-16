# CGI Common Gateway Interface support
# CGI 目前由 NCSA 维护
# CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等。
# https://docs.python.org/zh-cn/3/library/cgi.html
# https://www.runoob.com/python3/python3-cgi-programming.html
# 软件：IIS上配置CGI  https://blog.csdn.net/clhjswe/article/details/78213826
# 在iis中配置自己的cgi https://www.cnblogs.com/hualisuzhou/p/3589148.html
import cgi

form = cgi.FieldStorage()
user = form.getfirst("user", "").upper()  # This way it's safe.
for item in form.getlist("item"):
    print(item)
