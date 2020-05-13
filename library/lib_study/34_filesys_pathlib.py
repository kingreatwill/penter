from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath

p = Path('../')
print([x for x in p.iterdir() if x.is_dir()])
print(list(p.glob('*.py')))
print(list(p.glob('**/*.py')))

p = Path('/etc')
q = p / 'init.d' / 'reboot'  # 实现了__truediv__
print(q)  # \etc\init.d\reboot

print("------------class pathlib.PurePath(*pathsegments)")
print(PurePath())
pp = PurePath('34_filesys_pathlib.py')
print(pp)
print(PurePath('foo', 'some/path', 'bar'))
print(PurePath(Path('foo'), Path('bar')))
# 当给出一些绝对路径，最后一位将被当作锚（模仿 os.path.join() 的行为）:
print(PurePath('/etc', '/usr', 'lib64'))
print(PureWindowsPath('c:/Windows', 'd:bar'))
# 但是，在 Windows 路径中，改变本地根目录并不会丢弃之前盘符的设置:
print(PureWindowsPath('c:/Windows', '/Program Files'))

"""
>>> PurePosixPath('foo') == PurePosixPath('FOO')
False
>>> PureWindowsPath('foo') == PureWindowsPath('FOO')
True
>>> PureWindowsPath('FOO') in { PureWindowsPath('foo') }
True
>>> PureWindowsPath('C:') < PureWindowsPath('d:')
True
"""

print(
    PureWindowsPath('c:/Program Files/').drive,
    PureWindowsPath('/Program Files/').drive,
    PurePosixPath('/etc').drive,
    PureWindowsPath('//host/share/foo.txt').drive,
)

print(
    PureWindowsPath('c:/Program Files/').root,
    PureWindowsPath('c:Program Files/').root,
    PurePosixPath('/etc').root,
    PureWindowsPath('//host/share').root
)
