from calculator_function import add,sub,mul
a=int(input("enter first number:"))
b=int(input("enter second number:"))
inputData=input("select your choice(add,sub,mul,div):")
if inputData == "add":
    print(add(a,b))
elif inputData =="mul":
    mul(a,b)
elif inputData=="sub":
    sub(a,b)
elif inputData=="div":
    calculator_function.div(a,b)
