import random
a=[]
b=[]
for x in range(10):
    y=random.randint(0,100)
    z=random.randint(0,100)
    a.append(y)
    b.append(z)

for x in range(10):
    print(a[x]*b[x])
