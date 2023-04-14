count = 0
count_max = 0

for i in range(6):
    t = int(input(''))
    if t > 0:
        count += 1
    else:
        if count > count_max:
            count_max = count
        count = 0

print(count_max)
