# https://docs.python.org/zh-cn/3/library/compileall.html

# python -m compileall

# compileall.compile_dir(dir, maxlevels=10, ddir=None, force=False, rx=None, quiet=0, legacy=False, optimize=-1, workers=1, invalidation_mode=None)
# compileall.compile_file(fullname, ddir=None, force=False, rx=None, quiet=0, legacy=False, optimize=-1, invalidation_mode=None)
# compileall.compile_path(skip_curdir=True, maxlevels=0, force=False, quiet=0, legacy=False, optimize=-1, invalidation_mode=None)

# import compileall
#
# compileall.compile_dir('Lib/', force=True)
#
# # Perform same compilation, excluding files in .svn directories.
# import re
# compileall.compile_dir('Lib/', rx=re.compile(r'[/\\][.]svn'), force=True)
#
# # pathlib.Path objects can also be used.
# import pathlib
# compileall.compile_dir(pathlib.Path('Lib/'), force=True)