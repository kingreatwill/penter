# python -m tokenize 180_language_tokenize.py
import tokenize

with tokenize.open('180_language_tokenize.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)

import tokenize

with open('180_language_tokenize.py', 'rb') as f:
    tokens = tokenize.tokenize(f.readline)
    for token in tokens:
        print(token)