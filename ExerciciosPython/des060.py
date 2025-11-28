num = int(input('Digite um numero para ver o calculo do seu Fatorial: '))
cont = num
fat = 1
print(f'{num}!=', end=' ')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')
