"""
注解 从 Python 3.6 开始，不推荐使用 pyvenv 脚本，而是使用 python3 -m venv 来帮助防止任何关于虚拟环境将基于哪个 Python 解释器的混淆。
12.2. 创建虚拟环境
用于创建和管理虚拟环境的模块称为 venv。venv 通常会安装你可用的最新版本的 Python。如果您的系统上有多个版本的 Python，您可以通过运行 python3 或您想要的任何版本来选择特定的Python版本。

要创建虚拟环境，请确定要放置它的目录，并将 venv 模块作为脚本运行目录路径:

python3 -m venv tutorial-env
如果它不存在，这将创建 tutorial-env 目录，并在其中创建包含Python解释器，标准库和各种支持文件的副本的目录。

虚拟环境的常用目录位置是 .venv。 这个名称通常会令该目录在你的终端中保持隐藏，从而避免需要对所在目录进行额外解释的一般名称。 它还能防止与某些工具所支持的 .env 环境变量定义文件发生冲突。

创建虚拟环境后，您可以激活它。

在Windows上，运行:

tutorial-env\Scripts\activate.bat
在Unix或MacOS上，运行:

source tutorial-env/bin/activate
（这个脚本是为bash shell编写的。如果你使用 csh 或 fish shell，你应该改用 activate.csh 或 activate.fish 脚本。）

Activating the virtual environment will change your shell's prompt to show what virtual environment you're using, and modify the environment so that running python will get you that particular version and installation of Python. For example:

$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>

"""

# pip search astronomy
# pip 有许多子命令：“search”、“install”、“uninstall”、“freeze”等等
# https://docs.python.org/zh-cn/3/installing/index.html#installing-index
"""
pip install novas
pip install requests==2.6.0
pip install --upgrade requests
pip show requests
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
"""


"""
定制模块
Python提供了两个钩子来让你自定义它：sitecustomize 和 usercustomize。要查看其工作原理，首先需要找到用户site-packages目录的位置。启动Python并运行此代码:

>>>
>>> import site
>>> site.getusersitepackages()
'/home/user/.local/lib/python3.5/site-packages'
现在，您可以在该目录中创建一个名为 usercustomize.py 的文件，并将所需内容放入其中。它会影响Python的每次启动，除非它以 -s 选项启动，以禁用自动导入。

sitecustomize 以相同的方式工作，但通常由计算机管理员在全局 site-packages 目录中创建，并在 usercustomize 之前被导入。有关详情请参阅 site 模块的文档。
"""


