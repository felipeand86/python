r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os valores podem formar um triangulo,', end='')
    if r1 == r2 == r3:
        print(' Equilátero!')
    elif r1 != r2 != r3 != r1:
        print(' Escaleno!')
    else:
        print(' Isósceles!')
else:
    print('Não podem formar triângulo!')

