import random

a = random.sample(range(1, 20),10)

b = random.sample(range(1, 30),11)

c = []

for x in a:
    for y in b:
        if x == y and x not in c: c.append(x)
print("a: ",a)
print("b: ",b)
print("c: ",c)
