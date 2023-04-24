def order(num):
    if num < 10:
        return num
    print(num % 10, end='')
    return order(num // 10)

def rec(n):
    a = input()
    if n == 1:
        return a
    return rec(n - 1) + a


print(order(1230))
print(rec(5))
