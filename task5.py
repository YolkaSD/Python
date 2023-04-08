wagon_number_account = int(input('input wagon number: '))
wagon_number = int(input('input the number of the car in which you boarded: '))
summ = 0
if wagon_number_account == wagon_number:
    print()
else:
    summ = wagon_number_account + wagon_number - 1;
print(summ)