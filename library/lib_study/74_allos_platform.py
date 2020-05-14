import platform

print(platform.architecture())  # ('64bit', 'WindowsPE')
print(platform.machine())  # AMD64
print(platform.node())  # DESKTOP-PK520IC
print(platform.platform())  # Windows-10-10.0.18362-SP0
print(platform.processor())  # Intel64 Family 6 Model 158 Stepping 9, GenuineIntel
print(platform.python_build())  # ('tags/v3.7.6:43364a7ae0', 'Dec 19 2019 00:42:30')
print(platform.python_compiler())  # MSC v.1916 64 bit (AMD64)
print(platform.python_branch())  # tags/v3.7.6
print(platform.python_implementation())  # CPython
# Returns a string identifying the Python implementation. Possible return values are: 'CPython', 'IronPython', 'Jython', 'PyPy'.
print(platform.python_revision())  # 43364a7ae0
print(platform.python_version())  # 3.7.6
print(platform.python_version_tuple())  # ('3', '7', '6')
print(platform.release())  # 10
print(platform.system())  # Windows
print(platform.version()) # 10.0.18362
print(platform.system_alias("Windows", "10.0", "10.0.18362")) # ('Windows', '10.0', '10.0.18362') 有毛用？
print(platform.uname()) # uname_result(system='Windows', node='DESKTOP-PK520IC', release='10', version='10.0.18362', machine='AMD64', processor='Intel64 Family 6 Model 158 Stepping 9, GenuineIntel')
