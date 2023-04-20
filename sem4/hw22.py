m1 = 2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2
m2 = 3, 6, 9, 12, 15, 18
print(m1)
print(m2)

s = set()
for i in m1:
    s.add(i)
print(sorted(s))
