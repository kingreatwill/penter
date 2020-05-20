# Python模块浏览器支持
import pyclbr

print(pyclbr.readmodule("176_modules"))
print(pyclbr.readmodule_ex("176_modules"))

func1 = pyclbr.readmodule_ex("176_modules")["demo"]

print(func1.file)
print(func1.module)
print(func1.name)
print(func1.lineno)
print(func1.parent)
print(func1.children)