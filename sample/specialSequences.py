import re
txt="The rain in the Spain 100% in the plain"
#checking the string starts with "The"
x=re.findall("\AThe",txt)
print(x)
#check if ain is present at the beginning of a word
x1=re.findall(r"\bain",txt)
print(x1)
#opposite of \b:
x2=re.findall(r"\Bain",txt)
print(x2)
#to check if "ain" is present at the end of a word in the string
x3=re.findall(r"ain\b",txt)
print(x3)
#check if string contains a digit
x4=re.findall("\d",txt)
print(x4)
x5=re.findall("\D",txt)
print(x5)
#check about the spaces
x6=re.findall("\s",txt)
print(x6)
#check the words in a string
x7=re.findall("\w",txt)
print(x7)
x8=re.findall("\W",txt)
print(x8)
#check if the string ends with plain
x9=re.findall("plain\Z",txt)
print(x9)
if x9:
    print("yes! there is a match")
else:
    print("no match found")

