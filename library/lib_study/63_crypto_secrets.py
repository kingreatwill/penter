# secrets 模块可用于生成高加密强度的随机数，适应管理密码、账户验证、安全凭据和相关机密数据管理的需要。
#
# 特别地，应当优先使用 secrets 来替代 random 模块中默认的伪随机数生成器，后者被设计用于建模和仿真，而不适用于安全和加密。
import secrets
# 人们认为 32 字节（256 位）的随机性对于 secrets 模块所适合的典型用例来说是足够的。
# 参考 random.SystemRandom
sr = secrets.SystemRandom()
print(sr.random())

print(secrets.choice(["1", 2, "a"]))
print(secrets.randbelow(10))  # 返回一个 [0, n) 范围之内的随机整数。

print(secrets.token_bytes(16))
print(secrets.token_hex(16))
print(secrets.token_urlsafe(16))


# 生成长度为八个字符的字母数字密码:
import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
print(alphabet)
print(password)

# 生成长度为十个字符的字母数字密码，其中包含至少一个小写字母，至少一个大写字母以及至少三个数字:
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
print(password)

#生成 XKCD 风格的密码串:
#
# import secrets
# # On standard Linux systems, use a convenient dictionary file.
# # Other platforms may need to provide their own word-list.
# with open('/usr/share/dict/words') as f:
#     words = [word.strip() for word in f]
#     password = ' '.join(secrets.choice(words) for i in range(4))
#
# print(password)

#生成难以猜测的临时 URL，其中包含适合密码恢复应用的安全凭据:
print('https://mydomain.com/reset=' + secrets.token_urlsafe())