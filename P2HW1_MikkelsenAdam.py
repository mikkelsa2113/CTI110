# Code that calculates and displays travel expenses

# 10/19/2023

# CTI-110 P2HW1 - Travel Expense

# Adam Mikkelsen 

#Pseudocode:
#Input budget, destination, gas price, hotel price, food price
#Add expenses
#Compute final balance
#Output info



print('This is a program that calculates and displays travel expenses')
print()

user_bug = float(input('Enter Budget:\n'))
user_dest = str(input('Enter your travel destination:\n'))
user_gas = float(input('How much do you think you will spend on gas?\n'))
user_hotel = float(input('Approximately, how much will you need for accomodation/hotel?\n'))
user_food = float(input('Last, how much do you need for food?\n'))
print()

remain_bal = user_bug - (user_gas + user_food + user_hotel)

print('----------Travel Expenses----------')
print(f'Location:         ', user_dest)
print('Initial Budget:    ',end= '')
print(f'${user_bug:.2f}')
print('Fuel:              ',end='')
print(f'${user_gas:.2f}')
print('Accomodation:      ',end='')
print(f'${user_hotel:.2f}')
print('Food:              ',end='')
print(f'${user_food:.2f}')
print('-----------------------------------')

print('Remaining Balance: ',end='')
print(f'${remain_bal:.2f}')