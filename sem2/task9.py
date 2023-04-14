n = 5
f = 1
if n < 0:
    f = -1
else:
    i = 1
    while i <= n:
        f *= i
        i += 1
print(f)
