import re
count_lower=0
count_upper=0
txt=input("enter a string")
x=re.findall("[a-z]",txt)
print("lowercase letters are:")
for i in x:
    count_lower=count_lower +1
    print(i)
if x:
    print("no of lower case letters:",count_lower)
x1=re.findall("[A-Z]",txt)
print("upper case letters are:")
for j in x1:
    count_upper=count_upper+1
    print(j)
if x1:
    print("no of upper case letters:",count_upper)

#another method

"""x=input("enter a string")
countU=0
countL=0
for i in x:
    print(i)
    if i.isupper():
    
        countU+=1
    else:

        countL+=1
print("uppercase letters:",countU)
print("lowercase letters :",countL)

