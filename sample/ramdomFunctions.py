import random

print(random.choice([1, 2, 3, 4, 5, 6]))

print(random.randrange(20, 50, 3))

print(random.random())

random.seed(2)
print(random.random())


l1=[1,4,23,5,7,67]
random.shuffle(l1)
print(l1)


print(random.uniform(5,10))