import stringprep
import unicodedata

print(u'\ua62b')
print(unicodedata.category(u"\ua62b")) # Lo
print(stringprep.in_table_a1(u'\ua62b'))
print(stringprep.in_table_a1(chr(0x1F475)))

print(u'\ua62c') #꘬  因为没有定义 print(unicodedata.name(u"\ua62c"))
print(stringprep.in_table_a1(u'\ua62c'))
print(unicodedata.category(u"\ua62c")) # Cn
#https://baike.baidu.com/item/Unicode/750500?fr=aladdin
print(u'\u4e00')
# https://home.unicode.org/#
print(u'\uA755')
print(u'\u03c0')
print(chr(0x03c0))
print(chr(0x1F4AF)) # 💯

