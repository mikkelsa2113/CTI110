# Adam Mikkelsen
# P3HW1
# Code for the calculation of a grade


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


low = min(grades)
high = max(grades)
total = sum(grades)
avg = total/(len(grades))

# determine letter grade for average

print()
print('----------Results----------')
print('Lowest Grade:       ', low)
print('Highest Grade:      ', high)
print('Sum of Grades:      ', total)
print('Average:            ', avg)
print('---------------------------')
print()


if avg >= 90:
 print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg >=70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F')





