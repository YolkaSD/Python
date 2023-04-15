a = [1, 2, 3, 4, 5]
k = 2
# new_a = a[len(a) - k:] + a[:len(a) - k]
# print(new_a)

for i in range(k):
    a.insert(0, a.pop())

print(a)
