name = input('name: ')
labGrade = int(input('lab grade: '))
midGrade = int(input('midterm grade: '))
finalGrade = int(input('final grade: '))

lastScore = labGrade * 0.25 + midGrade * 0.35 + finalGrade * 0.40

print('Name: ' + name)
print('Lab Grade: ', labGrade)
print('Midterm Grade: ', midGrade)
print('Final Grade: ', finalGrade)
print('Last Score: ', lastScore)

