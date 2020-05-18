# pattern of Alphabets
rows=int(input("enter no of rows"))
num = 97  # 65 for upper case and 97 for lower case
for i in range(0,rows):
    for j in range(0,i+1):
        a=chr(num)
        print(a,end=' ')
        num=num+1
    print("\r")
