# CTI-110
# P4HW2 - Salary
# Adam Mikkelsen
# 11/28/23
# Code to calculate gross pay

#Pseudocode
#Input name, hours worked, pay rate
#calculate overtime
#calculate regular pay
#calculate gross pay
#print info
#ask if done - if yes, exit; if no, continue
#when done, show totals for all employees

done = int(1)
numEmps = int(0)
ovtTot = float(0)
regTot = float(0)
grossTot = float(0)

while done = 1:
    #input 
    userName = input('Enter employee name, or enter "Done" if you wish to exit: ')
    if userName == 'Done':
        break
    hrsWorked = float(input('Enter number of hours worked: '))
    payRate = float(input('Enter pay rate: '))

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
    
    #end totals
    numEmps += 1
    ovtTot += ovtPay
    regTot += regPay
    grossTot += grossPay

#print totals    
print()
print('Number of employees entered: ', numEmps)
print('Total amount paid in regular pay: ', regTot)
print('Total amount paid in overtime pay: ', ovtTot)
print('Total gross amount paid: ', grossTot)

