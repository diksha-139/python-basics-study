# number pyramid
num=1
rows=int(input("enter no of rows"))
for i in range(0,rows):
    for j in range(0,i+1):
        print(num,end=' ')
        num=num+1
    print("\r")