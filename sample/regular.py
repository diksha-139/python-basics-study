import re
txt="The rain in Spain"
x=re.search("^The .* Spain$", txt)

if x:
    print("yes! we got a match")
else:
    print("no match")

    x2 = re.search( "\s", txt )

    print( "the first white space is located at the position:", x2.start() )

#findall() function
x1=re.findall("ai",txt)
print(x1)

x3=re.split("\s",txt)
print(x3)

x4=re.sub("\s","90",txt)
print(x4)