
print(False)
print(True)
print(None)
print(NotImplemented)
print(Ellipsis)
print(__debug__) # 如果 Python 没有以 -O 选项启动，则此常量为真值。 python -O constants.py 则输出False
## 变量名 None，False，True 和 __ debug__ 无法重新赋值（赋值给它们，即使是属性名，将引发 SyntaxError ），所以它们可以被认为是“真正的”常数。


## 下面的静态变量由site模块自动导入，除非加上-S参数  python -S constants.py  :NameError: name 'copyright' is not defined

print(copyright)
print(credits)
print(license)
quit()
exit()