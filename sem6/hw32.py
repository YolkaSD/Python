arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
td = (7, 11)

for i in range(len(arr)):
    if td[0] <= arr[i] <= td[1]:
        print(i)
