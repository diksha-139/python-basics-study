l1 = [8,2,5,70,8,67,11,23]
"""print(max(l1))
print(sorted(l1))
print(l1[-1])"""


temp=0
for i in l1:
    if temp < i:
        temp = i
    else:
        continue
print("largest:",temp)
