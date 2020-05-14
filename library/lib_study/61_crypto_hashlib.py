import hashlib

m = hashlib.sha256()
m.update(b"Nobody inspects")  # 哈希基于字节而非字符
m.update(b" the spammish repetition")
print(m.digest())
print(m.digest().hex())
print(m.hexdigest())
print(hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())

print(m.digest_size)
print(m.block_size)
print("--------------")
print(hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest())
h = hashlib.new('sha224')
h.update(b"Nobody inspects the spammish repetition")
print(h.hexdigest())

print("--------------")
h = hashlib.new('ripemd160')
h.update(b"Nobody inspects the spammish repetition")
print(h.hexdigest())

print("--------------")
print(hashlib.algorithms_guaranteed)
# {'sha3_512', 'md5', 'sha3_384', 'sha3_224', 'shake_256', 'sha384', 'sha224', 'blake2s', 'sha1', 'sha512', 'sha256', 'blake2b', 'sha3_256', 'shake_128'}
print(hashlib.algorithms_available)
# {'sha3_384', 'blake2b', 'sha3_256', 'sha3_224', 'md5', 'sha3_512', 'sha384', 'shake_128', 'shake_256', 'sha512', 'blake2s', 'sha224', 'sha1', 'sha256'}
print("--------------")
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
print(dk.hex())

st = hashlib.scrypt(b'password', salt=b'salt', n=2, r=16, p=9)
print(st.hex())
