# data type conversion

a = 123
b = 1.23
s = a + b
print("sum is :", s, type(s))

# explicit
x = 123
y = "456"
r = str(x)+y
print("datatype of x:", type(x))
print("data type of y:", type(y))
print("datatype and value of sum is:", type(r), r)

s = x+int(y)
print("sum value and data type  is :", s, type(s))
