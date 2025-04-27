import random
a=[]
s=[]
d=0
for i in range(10):
    a.append(random.randint(1,5))
for j in range(10):
    s.append(a[j]*4)
    if s[j]>10:
        d=d+s[j]
print(d)
