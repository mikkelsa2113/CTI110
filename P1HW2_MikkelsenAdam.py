# Code that calculates and displays travel expenses

# 10/03/2023

# CTI-110 P1HW2 - Travel Expense

# Adam Mikkelsen 



print('This is a program that calculates and displays travel expenses')
print()

user_bug = float(input('Enter Budget:\n'))
user_dest = str(input('Enter your travel destination:\n'))
user_gas = float(input('How much do you think you will spend on gas?\n'))
user_hotel = float(input('Approximately, how much will you need for accomodation/hotel?\n'))
user_food = float(input('Last, how much do you need for food?\n'))
print()

remain_bal = (((user_bug - user_gas) - user_food) - user_hotel)

print('----------Travel Expenses----------')
print('Location:', user_dest)
print('Initial Budget: $',user_bug)
print()

print('Fuel: $',user_gas)
print('Accomodation: $',user_hotel)
print('Food: $',user_food)
print()

print('Remaining Balance: $',remain_bal)