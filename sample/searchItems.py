list=["anitha", "sunita", "Amrita", "y", "anna", "diksha"]
count=0
for i in list:

    if len(i)>2 and i[0]==i[-1]:
        print(i)
        count=count+1

print("there are {} no of items having first and last character same".format(count))