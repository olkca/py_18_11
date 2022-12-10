from random import randint
a = []
b = []
c = []
i = 0
while i in range(10):
    a.append(randint(0, 10))
    b.append(randint(0, 10))
    c = list(set(a) & set(b))
    i += 1
print(a)
print(b)
print(c)
