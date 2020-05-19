# https://docs.python.org/zh-cn/3/library/exceptions.html#warnings
# 默认警告过滤器
# By default, Python installs several warning filters, which can be overridden by the -W command-line option,
# the PYTHONWARNINGS environment variable and calls to filterwarnings().

"""
default                      # Show all warnings (even those ignored by default)
ignore                       # Ignore all warnings
error                        # Convert all warnings to errors
error::ResourceWarning       # Treat ResourceWarning messages as errors
default::DeprecationWarning  # Show DeprecationWarning messages
ignore,default:::mymodule    # Only report warnings triggered by "mymodule"
error:::mymodule[.*]         # Convert warnings to errors in "mymodule"
                             # and any subpackages of "mymodule"

default::DeprecationWarning:__main__
ignore::DeprecationWarning
ignore::PendingDeprecationWarning
ignore::ImportWarning
ignore::ResourceWarning

可以从命令行通过传递 -Wd 参数到解释器（即为 -W default 的速记）。
这将为所有警告启用默认处理，包括默认情况下忽略的警告。
要更改遇到的警告所采取的操作，只需更改传递给 -W 的参数即可，如 -W error。
可以用 python --help 来查看 -W 参数的详细使用。

在代码中实现 -Wd 的功能为:

warnings.simplefilter('default')

"""




# import sys
#
# if not sys.warnoptions:
#     import warnings
#
#     warnings.simplefilter("ignore")
#
# import sys
#
# if not sys.warnoptions:
#     import os, warnings
#
#     warnings.simplefilter("default")  # Change the filter in this process
#     os.environ["PYTHONWARNINGS"] = "default"  # Also affect subprocesses
#
#
# import warnings
# warnings.filterwarnings("default", category=DeprecationWarning,
#                                    module=user_ns.get("__name__"))

# import warnings
#
# def fxn():
#     warnings.warn("deprecated", DeprecationWarning)
#
# with warnings.catch_warnings(record=True) as w:
#     # Cause all warnings to always be triggered.
#     warnings.simplefilter("always")
#     # Trigger a warning.
#     fxn()
#     # Verify some things
#     assert len(w) == 1
#     assert issubclass(w[-1].category, DeprecationWarning)
#     assert "deprecated" in str(w[-1].message)
#
