import hashlib
myString=input("enter a string")
hashObject=hashlib.md5(myString.encode())
print(hashObject.hexdigest())