arr = [1, 2, 3, 2, 3, 2, 3]
count = 0

for i in range(len(arr)):
    for j in arr[i + 1:]:
        if arr[i] == j:
            count += 1

print(count)
