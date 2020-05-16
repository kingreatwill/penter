# https://docs.python.org/zh-cn/3/library/mimetypes.html
import mimetypes

mimetypes.init()
print(mimetypes.knownfiles)

print(mimetypes.suffix_map['.tgz'])

print(mimetypes.encodings_map['.gz'])

print(mimetypes.types_map['.tgz'])
