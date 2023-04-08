x1 = int(input('x1: '))
y1 = int(input('y2: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

if 0 < x1 <= 8 and 0 < x2 <= 8 and 0 < y1 <= 8 and 0 < y2 <= 8:
    if abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
        print('Y')
    elif abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
        print('Y')
    else:
        print('No')
