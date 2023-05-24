# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
#
#
# print(res)


# def even(arr1, is_even):
#     d = dict()
#     for i in arr1:
#         if is_even(i):
#             d[i] = i * i
#     return d
#
#
# print(even(arr, lambda n: n % 2 == 0))

# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
#
# res = where(lambda x: x % 2 == 0, data)
# print(res)
#
# res = select(lambda x: (x, x ** 2), res)
# print(res)


# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = '1 123 15 126 21 51 21 51 23 31'
# print(data)
#
# print(data.split(' '))
#
# data = list(map(int, data.split()))
# print(data)

# data = [1, 4, 3, 9, 4, 8, 1, 0, 3, 5, 2, 9]
#
# data = list(filter(lambda x: x >= 5, data))
# print(data)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# data = list(map(lambda x: [x, x ** 2], filter(lambda x: x % 2 == 0, data)))
# print(data)