fillingDesks = 2
grade = 3
countGrade = 0
for i in range(grade):
    numStudentGrade = int(input("Number of students in the grade: "))
    # countGrade += numStudentGrade / fillingDesks
    # countGrade += numStudentGrade // fillingDesks + numStudentGrade % 2
    countGrade += (numStudentGrade + 1 // fillingDesks)

# if countGrade % 2 != 0:
#     countGrade = int(countGrade) + 1

print('Requires {} grade'.format(countGrade))
