import random
list1 = []
list2 = []
n=10
for i in range(n):
    list1.append(random.randint(0,10))
    list2.append(random.randint(0,10))
print(list1)
print(list2)
res = list(set(list1+list2))
print(res)
