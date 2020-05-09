# 内置 包含外部的functions，constants，stdtypes文件夹的内容

# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p09_normalize_unicode_text_to_regexp.html

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)  # 创建一个新的字典
merged.update(a)  # update进入的键值会覆盖原来的键值对
print(merged)
merged['x'] = 10
print(a)
a['x'] = 12  # 更改老字典，新创建的merged不会改变
print(a)