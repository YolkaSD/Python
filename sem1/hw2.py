num = 123
digit_summ = 0
num_digits = len(str(num))

for i in range(num_digits):
    digit_summ += num % 10
    num //= 10

print(digit_summ)
