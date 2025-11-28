n = int(input('Digite um numero: '))
fat = 1
calc = ''
for i in range(n, 0, -1):
    fat *= i
    if i > 1:
        calc += f'{i} x '
    else:
        calc += f'{i} = '
calc += str(fat)
print(calc)

