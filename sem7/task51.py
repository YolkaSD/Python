values = [0, 2, 10, 6, 2]


def same_by(f, arr):
    # for i in arr:
    #     if f(i):
    #         continue
    #     else:
    #         return False
    # return True
    return len(list(filter(f, arr))) == 0


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
