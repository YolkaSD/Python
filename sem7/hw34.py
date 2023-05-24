poem = 'пара-ра-рам рам-пам-папам па-ра-па-да папапа-па'.split()
lst = list()

for i in poem:
    lst.append(i.count('а'))

if all(x == lst[0] for x in lst):
    print('Парам пам-пам')
else:
    print('Парам пам')

