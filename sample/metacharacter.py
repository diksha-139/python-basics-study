import re

txt = "The rain 100 in Spain"
# find all the alphabets between a-m
x = re.findall( "[a-m]", txt )
print( x )

txt1 = "That will be 300 dollars"
# find all digits
x1 = re.findall( "\d", txt1 )
print(x1)

txt2 = "hello world"
x2=re.findall("he..o",txt2)
print(x2)
# finds hello as starting word

x3=re.findall("^hello",txt2)

# find world as last word
x4=re.findall("world$",txt2)
print(x4)

txt3= "The rain in Spain falls mainly in 100% plain"
#checking if the string contains either "falls" or "stays":
x5=re.findall("falls|stays",txt3)
print(x5)

#checking if string contains "ai" followed by 0 or more x characters

x6=re.findall("aix*",txt3)
print(x6)

#checking if string contains "ai" followed by 0 or more x characters
x7=re.findall("aix+",txt3)
print(x7)
# check number of occurences of any character
x8=re.findall("al{2}",txt3)
print(x8)