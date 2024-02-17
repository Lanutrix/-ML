from itertools import product as pr
c = 2
f=0
p = pr("ЛОСЬ",repeat=5)
for i in p:
    s = "".join(i)
    if s=="ОЛЬСЬ":
        f = 1
    if f:
        c+=1
    if s=="СОЬЬЛ":
        f = 0

print(c)