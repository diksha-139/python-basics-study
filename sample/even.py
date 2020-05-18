list = [1,34,12,34,5,67,8,23]


print("list of even numbers :")
count=0
for x in list:
    if(x % 2 == 0):
        count=count+1
        print(x)
print("number of even numbers = ",count)
