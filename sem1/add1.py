number = int(input('Enter the number: '))
output = ""
is_zero = False
if number > 0:
    output += 'positive'
elif number < 0:
    output += 'negative'
else:
    is_zero = True
    output += 'zero'

if not is_zero:
    if number % 2 == 0:
        output += ' even'
    else:
        output += ' odd'
output += ' number'
print(output)
