import unicodedata

# https://www.unicode.org/reports/tr44/
# http://www.unicode.org/Public/12.1.0/ucd/NameAliases.txt
# http://www.unicode.org/Public/12.1.0/ucd/NamedSequences.txt
# https://home.unicode.org/
# unicode字符表 http://www.unicode.org/charts/
# UCD是Unicode字符数据库（Unicode Character DataBase）的缩写。
# 在UCD 5.0,0中，Unihan.txt文件大小有28,221K字节。Unihan.txt中包含了很多有参考价值的索引，例如汉字部首、笔划、拼音、使用频度、四角号码排序等。这些索引都是基于一些比较权威的辞典，但大多数索引只能检索部分汉字。
print(unicodedata.lookup('LEFT CURLY BRACKET'))
print(unicodedata.name('{'))
print(unicodedata.name('㚇'))
print(unicodedata.name('\n', 0))  # 未找到对应名称，返回'0'

print(unicodedata.decimal('7'))
print(unicodedata.digit('7'))
print(unicodedata.numeric('壹'))
print(unicodedata.numeric('四'))
print(unicodedata.numeric('8'))

# 返回字符chr在unicode里分类的类型。具体类型见文档结尾附录1。
print(unicodedata.category('四'))  # Letter, Other
print(unicodedata.category('8'))  # Number, Decimal Digit
# unicodedata.category('A')  # 'L'etter, 'u'ppercase
# unicodedata.bidirectional('\u0660') # 'A'rabic, 'N'umber
print(unicodedata.bidirectional(u'\u0660'))  # 'A'rabic, 'N'umber
print(unicodedata.bidirectional('8'))  # EN
print("-------------------")
t1 = unicodedata.normalize('NFD', 'Spicy Jalape\u00f1o')
print(t1)
print("-------------------")
for c in t1:
    print(c)
print("-------------------")
for c in t1:
    if not unicodedata.combining(c):
        print(c)
print("-------------------")
# 重音符号（变音符号）
print(''.join(c for c in t1 if not unicodedata.combining(c)))
print("-------------------")

# 将unicode字符串unistr进行规范化。规范形式form有四种：NFC、NFD、NFKC和NFKD。将字符串规范化是为了方便存储文本或者比较字符串而设计的。

accented_string = u'Málaga'
print(unicodedata.normalize('NFD', accented_string))

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(unicodedata.normalize('NFC', s1))
print(unicodedata.normalize('NFC', s2))
print(ascii(unicodedata.normalize('NFC', s1)))

print(unicodedata.normalize('NFD', s1))
print(unicodedata.normalize('NFD', s2))
print(ascii(unicodedata.normalize('NFD', s1)))
s = '\ufb01'  # A single character
print(unicodedata.normalize('NFKC', s))
print(ascii(unicodedata.normalize('NFKC', s)))

print(unicodedata.normalize('NFKD', s))
print(ascii(unicodedata.normalize('NFKD', s)))

s1 = 'café' # 'é'为组合字符，由'e'与重音符组合而成
s2 = 'cafe\u0301' # 将'é'拆为'e'和'\u0301'，'\u0301'为重音符的unicode编码

print(unicodedata.normalize('NFC', s1)) # NFC使用最少的码位，所以'é'被合并为一个字符(事实上s1中本来就是é)，因而返回结果为'café'(输出不带引号)
print(unicodedata.normalize('NFC', s2)) # 'e'和'\u0301'被合并为一个字符é，因而返回结果为'café'(输出不带引号)
print(unicodedata.normalize('NFD', s1)) # NFD使组合字符拆开为两个字符，这里'é'被拆为'e'和重音符，即输出结果为:'cafeˋ'
print(unicodedata.normalize('NFD', s2)) # s2最后两个字符为'e'和'\u0301'，（我不知道内部机理是什么，接下来的叙述是我自己的理解，不知道正确与否），直接将'\u0301'解释为重音符'ˋ'，输出为'cafeˋ'

print("-------------------")
print(unicodedata.east_asian_width('我'))
print(unicodedata.east_asian_width('1'))
print(unicodedata.east_asian_width('a'))
print(unicodedata.east_asian_width('ﷺ'))
# F：fullwidth，H：halfwidth，W：wide，Na：narrow，A：ambiguous(不明确)，N：natural(正常)


print(unicodedata.mirrored('薛')) # 不懂

print(unicodedata.decomposition('ﷺ')) # 可分解
print(unicodedata.decomposition('é')) # 可分解
print(unicodedata.decomposition('e')) # 不可分解，所以返回空值（输出就是一片空白）

# 判断 Unicode 字符串 unistr 是否为正规形式 form。 form 的有效值为 'NFC', 'NFKC', 'NFD' 和 'NFKD'
# 3.8
# print(unicodedata.is_normalized('NFC','a')) # true
# print(unicodedata.is_normalized('NFC','ﷺ')) # true
# print(unicodedata.is_normalized('NFKD','ﷺ')) # false

print(unicodedata.unidata_version)
print(unicodedata.ucd_3_2_0)

#print('const CATEGORY_e CHAR_CATEGORIES[] = {%s};' % ', '.join(unicodedata.category(chr(codepoint)) for codepoint in range(0x110000)))


print(u'\ua62c') #꘬  因为没有定义 print(unicodedata.name(u"\ua62c"))
print(unicodedata.category(u"\ua62c")) # Cn
#https://baike.baidu.com/item/Unicode/750500?fr=aladdin
print(u'\u4e00')
# https://home.unicode.org/#
print(u'\uA755')
print(u'\u03c0')
print(chr(0x03c0))
print(chr(0x1F4AF)) # 💯

