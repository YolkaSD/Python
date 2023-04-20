string = 'a a a b c a a d c d d'.split(' ')
string2 = ''
for i in string:
    v = string2.count(i)
    if v != 0:
        string2 += i + '_' + str(v) + ' '
    else:
        string2 += i + ' '
print(string2)


d = {}
for i in string:
    if i in d:
        d[i] += 1
        print(f'{i}_{d[i]}', end=' ')
    else:
        d[i] = 0
        print(i, end=' ')
