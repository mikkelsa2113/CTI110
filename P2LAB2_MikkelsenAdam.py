num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

intProd = float(num1 * num2 * num3 * num4)
intAve = float((num1 + num2 + num3 + num4)/4)

fltProd = float(num1 * num2 * num3 * num4)
fltAve = float((num1 + num2 + num3 + num4)/4)

print(f'{intProd:.0f} {intAve:.0f}')
print(f'{fltProd:.3f} {fltAve:.3f}')
