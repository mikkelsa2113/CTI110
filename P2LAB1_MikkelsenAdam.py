milage = float(input())
gasCost = float(input())

val1 = float((20 / milage) * gasCost)
val2 = float((75 / milage) * gasCost)
val3 = float((500 / milage) * gasCost)

print(f'{val1:.2f} {val2:.2f} {val3:.2f}')
