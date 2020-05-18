import re
txt=input("enter a string")
l1=[]
l2=[]
def vowel(n):
    x=re.findall("[aeiouAEIOU]",n)
    x1=re.findall("[^aeiouAEIOU]",n)

    if x:
        l1.append(x)
        print("vowel present in",n," is",l1)

    if x1:
        l2.append(x1)
        print("consonants present are",l2)

vowel(txt)