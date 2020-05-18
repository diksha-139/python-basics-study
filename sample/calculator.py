import calculator_function
a=input("enter first number:")
b=input("enter second number:")
inputData=input("select your choice(add,sub,mul,div):")
if inputData == "add":
    print(calculator_function.add(a,b))
elif inputData =="mul":
    calculator_function.mul(a,b)
elif inputData=="sub":
    calculator_function.sub(a,b)
elif inputData=="div":
    calculator_function.div(a,b)