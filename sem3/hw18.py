a = [1, 2, 3, 4, 5, -7]
x = 6
min_diff = abs(a[0] - x)
c = None
for i in range(1, len(a)):
    if min_diff > abs(a[i] - x):
        c = a[i]

print(c)
