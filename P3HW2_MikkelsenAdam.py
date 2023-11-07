# CTI-110
# P3HW2 - Salary
# Adam Mikkelsen
# 11/07/23
# Code to calculate gross pay

#Pseudocode
#Input name, hours worked, pay rate
#calculate overtime
#calculate regular pay
#calculate gross pay
#print info

#input 
userName = input('Enter your name: ')
hrsWorked = float(input('Enter number of hours worked: '))
payRate = float(input('Enter your pay rate: '))

#overtime
if hrsWorked > 40:
    ovt = float(hrsWorked - 40)
    ovtPay = float(ovt * (payRate * 1.5))
else:
    ovt = float(0)
    ovtPay = float(0)

#regular pay
regHrs = float(hrsWorked - ovt)
regPay = float(regHrs * payRate)

#gross pay
grossPay = float(regPay + ovtPay)

#print info
print('----------------------------------')
print('Employee Name:   ',userName)
print()
print('Hours worked   Pay Rate    Overtime    Overtime Pay    Regular Pay    Gross Pay    ')
print('------------------------------------------------------------------------------------')
print(f'{hrsWorked:<15.2f}{payRate:<12.2f}{ovt:<12.2f}${ovtPay:<15.2f}${regPay:<14.2f}${grossPay:<13.2f}')
