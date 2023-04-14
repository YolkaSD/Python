n = 5

if n == 0:
    print(1)
elif n == 1:
    print(2, 3)
else:
    a, b = 1, 2
    count = 4
    while n >= a + b:
        b, a, count = a + b, b, count + 1
        if b == n:
            print(count)
            break
    else:
        print(-1)
