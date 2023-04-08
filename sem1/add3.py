a = int(input())
b = int(input())
c = int(input())

if c < a + b and b < a + c and a < b + c:
    print('Triangle exists')
else:
    print('Triangle does not exist')
