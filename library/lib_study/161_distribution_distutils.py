"""
setuptools 是一个对于 distutils 的增强选项，它能提供：

对声明项目依赖的支持

额外的用于配置哪些文件包含在源代码发布中的机制（包括与版本控制系统集成需要的插件）

生成项目“进入点”的能力，进入点可用作应用插件系统的基础

自动在安装时间生成 Windows 命令行可执行文件的能力，而不是需要预编译它们

跨所有受支持的 Python 版本上的一致的表现



推荐的 pip 安装器用 setuptools 运行所有的 setup.py 脚本，即使脚本本身只引了 distutils 包。参考 Python Packaging User Guide  获得更多信息。
https://packaging.python.org/
"""
import distutils

