import zipimport

# zi = zipimport.zipimporter("foo/bar.zip")
# zi.find_module("")

"""
这是一个从 ZIP 档案中导入模块的例子 - 请注意 zipimport 模块不需要明确地使用。

$ unzip -l example.zip
Archive:  example.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     8467  11-26-02 22:30   jwzthreading.py
 --------                   -------
     8467                   1 file
$ ./python
Python 2.3 (#1, Aug 1 2003, 19:54:32)
>>> import sys
>>> sys.path.insert(0, 'example.zip')  # Add .zip file to front of path
>>> import jwzthreading
>>> jwzthreading.__file__
'example.zip/jwzthreading.py'
"""