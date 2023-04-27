k = int(input(''))
dct = dict()

nums = list()

# for n in range(1, k):
#     m = 0
#     summ2 = 0
#     for i in range(1, n):
#         if n % i == 0:
#             m += i
#     for j in range(1, m):
#         if m % j == 0:
#             summ2 += j
#     if summ2 == n and n < m:
#         print(n, m)


for i in range(k):
    summ = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summ += j
            nums.append([i, summ])
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i][0] == nums[j][1] and nums[i][1] == nums[j][0] and i != j:
            print(*nums[i])
