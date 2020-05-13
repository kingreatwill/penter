import linecache


print(linecache.checkcache("42_filesys_linecache.py"))
print(linecache.checkcache())

print(linecache.getline("42_filesys_linecache.py",1))
print(linecache.getline(__file__, 1))
print(linecache.__file__)
print(linecache.getline(linecache.__file__, 8))