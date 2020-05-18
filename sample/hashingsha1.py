import hashlib
hashObject=hashlib.sha1(b"Hello World")
hexDigit=hashObject.hexdigest()
print(hexDigit)