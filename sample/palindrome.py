a=input("enter a string")
print(type(a))
length=len(a)
while length>0:
    temp=a[length-1]
    length=length-1
    print(temp)
for x in a:
    temp1=[]
    temp1=x
if temp1==temp:
    print("palindrome")
else:
    print("not palindrome")




