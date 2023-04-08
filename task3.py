import math

fillingDesks = 2
grade = 3
countGrade = 0
for i in range(grade):
    numStudentGrade = int(input("Number of students in the grade: "))
    countGrade += math.ceil(numStudentGrade/fillingDesks)
print('Requires {} grade'.format(countGrade))
