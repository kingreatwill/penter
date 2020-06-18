"""
https://snarky.ca/the-many-ways-to-pass-code-to-python-from-the-terminal/
# 管道传内容给 python
echo "print('hi')" | python

# 重定向一个文件给 python
python < spam.py


# 使用 python 的 -c 参数
python -c "print('hi')"

# 指定 python 的文件路径
python spam.py

# 对包使用 -m
python -m spam
它在底层使用了runpy[5]。要在你的项目中做到这点，只需要在包里指定一个__main__.py文件，它将被当成__main__执行。而且子模块可以像任何其它模块一样导入，因此你可以对其进行各种测试。
有些人喜欢在一个包里写一个main子模块，然后将其__main__.py写成：
from . import main
if __name__ == "__main__":
    main.main()


# 目录
定义__main__.py也可以扩展到目录。如果你看一下促成此博客文章的示例，python news可执行，就是因为 news 目录有一个 __main__.py文件。该目录就像一个文件路径被 Python 执行了。

import runpy
# Change 'announce' to whatever module you want to run.
runpy.run_module('announce', run_name='__main__', alter_sys=True)

# 执行一个压缩文件
# 将一个压缩包传给 Python
python app.pyz
如果你确实有多个文件和/或依赖模块，并且希望将所有代码作为一个单元发布，你可以用一个__main__.py，放置在一个压缩文件中，并把压缩文件所在目录放在 sys.path 里，Python 会替你运行__main__.py文件。
"""