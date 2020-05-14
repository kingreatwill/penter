# 便携式密码输入工具
import getpass

# getpass.getpass(prompt='Password: ', stream=None)

print(getpass.getuser())
# 此函数会按顺序检查环境变量 LOGNAME, USER, LNAME 和 USERNAME，并返回其中第一个被设置为非空字符串的值。
#此函数应优先于 os.getlogin() 使用