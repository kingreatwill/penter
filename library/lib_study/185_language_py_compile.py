# py_compile.compile(file, cfile=None, dfile=None, doraise=False, optimize=-1, invalidation_mode=PycInvalidationMode.TIMESTAMP, quiet=0)

import py_compile
# py_compile.compile()

"""
```
import py_compile

py_compile.compile(file = "a.py",cfile = "a.pyc",optimize=-1)

py_compile.compile(file = "b.py",cfile = "b.pyo",optimize=1)
```
也可以直接通过Python加载模块来运行：
```
#编译成pyc
python -m py_compile 源代码

#编译成pyo

python -O -m py_compile 源代码
```
"""