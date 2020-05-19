"""
$ python -m zipapp myapp -m "myapp:main"
$ python myapp.pyz
<output from myapp>

# 打包依赖
python -m pip install -r requirements.txt --target myapp

# http://c.biancheng.net/view/2687.html
"""


from distutils.ccompiler import new_compiler
import distutils.sysconfig
import sys
import os
from pathlib import Path

def compile(src):
    src = Path(src)
    cc = new_compiler()
    exe = src.stem
    cc.add_include_dir(distutils.sysconfig.get_python_inc())
    cc.add_library_dir(os.path.join(sys.base_exec_prefix, 'libs'))
    # First the CLI executable
    objs = cc.compile([str(src)])
    cc.link_executable(objs, exe)
    # Now the GUI executable
    cc.define_macro('WINDOWS')
    objs = cc.compile([str(src)])
    cc.link_executable(objs, exe + 'w')

if __name__ == "__main__":
    compile("zastub.c")