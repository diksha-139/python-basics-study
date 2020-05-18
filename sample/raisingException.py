try:
    num=int(input("enter a number"))
    if num<=5:
        raise Exception("\n num should be greater than 5")
except Exception as e:
    print("error",e)
else:
    print(num,"is greater than 5")