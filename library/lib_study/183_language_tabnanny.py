import tabnanny
import tokenize

print(tabnanny.verbose)

print(tabnanny.filename_only)

# 检查文件缩进问题.
print(tabnanny.check('180_language_tokenize.py'))

# with open('180_language_tokenize.py', 'rb') as f:
#     tokens = tokenize.tokenize(f.readline)
#     print(tabnanny.process_tokens(tokens))
#     for token in tokens:
#         print(tabnanny.process_tokens(token))
