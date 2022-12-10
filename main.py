import random
a = []
b = []
c = []
n=10
for i in range(n):
    a.append(random.randint(-100,100))
    b.append(random.randint(-100,100))
print(a)
print(b)
for i in a:
    if i in b and i not in c:
        c.append([i])
print(c) #реба запустити екілька разів щоб повезло на цифри
