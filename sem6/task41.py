arr = [1, 5, 1, 5, 1]
num = 5
count = 0

if len(arr) > 2:
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            count += 1
print(count)
