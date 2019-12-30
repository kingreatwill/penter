import re

pat = "p.*y"  # pat就是贪婪模式
pat2 = "p.*?y"  # pat2就是懒惰模式
str = "safpdfgysffpzvbqby"
aaa = re.search(pat, str)
print(aaa)

bbb = re.search(pat2, str)

print(bbb)


# re.match函数要从头开始匹配
pat="python"

string="psgsfpython"

string1="pythonsfdf"

aaa = re.match(pat,string)

print(aaa)

bbb = re.match(pat,string1)

print (bbb)


print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))