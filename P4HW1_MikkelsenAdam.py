# CTI-110
# P4HW1 - Score List
# Adam Mikkelsen
# 11/21/23
# Pseudocode:
# Enter number of grades. Enter grades. Calculate min, average, letter grade. Print results.
  
print('How many scores would you like to enter?')
numGrades = int(input('Enter: '))
print()
  
run = int(1)
gradeList = []
  
while run <= numGrades :
    print('Enter Grade #',run,':', end = '')
    grade = float(input())
    if (grade >=0) and (grade <=100):
        gradeList.append(grade)
        run +=1
    else :
        print('Invalid Score. Please try again')

avg = float((sum(gradeList))/numGrades)
gradeMin = float(min(gradeList))

compGrade = 'F'

if avg >=90:
    compGrade = 'A'
elif avg >=80:
    compGrade = 'B'
elif avg >=70:
    compGrade = 'C'
elif avg >=60:
    compGrade = 'D'


print('----------Results----------')
print('Lowest Score :', gradeMin)
print('Modified List:', gradeList)
print('Score Average:', avg)
print('Grade        :', compGrade)
print('---------------------------')



