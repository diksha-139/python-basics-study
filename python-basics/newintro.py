a=10
print(a,type(a))
print(isinstance(a,int))

print(isinstance(a,float))


#methods
animal=["cat","dog","rabbit","monkey"]
animal.append("pig")
print(animal)
animal.insert(2,"lion")

animal.remove("pig")

array=[1,2,3,4,1,1,2,2,4,7,8,9]

array.count(2)

print("count",array.count(2))

array.remove(1)

print(array)
my_tuple=('h','e','l','o','h',1,5,6)
print(my_tuple)
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[0:4])
print("count",my_tuple.count('h'))