n = 10011011000
c1, c2 = 0, 0
for i in str(n):
    if i == '1':
        c1 += 1
    else:
        c2 += 1

if c1 > c2:
    print(c2)
else:
    print(c1)
