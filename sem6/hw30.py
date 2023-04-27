first_num = 7
diff = 2
count_num = 5
lst = [first_num]

for i in range(count_num - 1):
    lst.append(lst[i] + diff)

print(lst)