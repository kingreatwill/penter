import hashlib
import hmac

h = hmac.new(b"123",b"datdtadtad")
print(h)
print(h.hexdigest())

print(hmac.digest(b"123",b"datdtadtad",hashlib.md5).hex())