import random
list1 = []
list2 = []
n=10
for i in range(n):
    list1.append(random.randint(3,9))
    list2.append(random.randint(3,9))
print(list1)
print(list2)
list3 = list1 + list2
print(list3)
