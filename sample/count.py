a="diksha,sruthi,anju,anita,anupma"
#a=input("enter names seperated by comma")
temp=a.split(",")
i=0
while i < a.count(",")+1:
    res=0
    res=temp[i]

    if res[0]==res[-1] and len(res)>=2:
        print( res )
    i=i+1

