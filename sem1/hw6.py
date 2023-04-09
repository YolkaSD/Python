number = 385916
first_three_digits = number // 1000
last_three_digits = number % 1000

sum_first_three_digits = sum(int(digit) for digit in str(first_three_digits))
sum_last_three_digits = sum(int(digit) for digit in str(last_three_digits))


if sum_first_three_digits == sum_last_three_digits:
    print('YES')
else:
    print('NO')



