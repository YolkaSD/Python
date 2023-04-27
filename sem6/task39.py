size_arr1 = 7
arr1 = [3, 1, 3, 4, 2, 4, 12]
size_arr2 = 6
arr2 = [4, 15, 43, 1, 15, 1]

# for i in arr1:
#     check = False
#     for j in arr2:
#         if i == j:
#             check = True
#     if not check:
#         print(i)

for i in arr1:
    if i not in arr2:
        print(i, end='')
