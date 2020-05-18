# if else conditional statements

a = input("enter first number:")
b = input("enter second number")
if a > b:
    print("{} is greater than{}".format(a, b))
elif a == b:
    print("both{}and{} are equal".format(a, b))
else:
    print("{}is greater than{}".format(b, a))

