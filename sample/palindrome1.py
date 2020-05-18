a=input("enter any string")
rev=a[::-1]
print(rev)
if a==rev:
    print('palindrome')
else:
    print("not palindrome")