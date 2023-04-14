s = 112 + 356 #int(input("Введите сумму чисел: "))
p = 112 * 356 ##int(input("Введите произведение чисел: "))

print(s, p)

for x in range(1, 1001):
    if p % x == 0:
        y = p // x
        if x + y == s:
            print("Ответ: x =", x, ", y =", y)
            break
else:
    print("Нет решения для заданных условий.")

