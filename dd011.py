resp = 's'
while resp == 's':
    num = int(input('Digite um número: '))
    dig = num * 2
    print(num)
    print(dig)
    resp = input(('Quer continuar? (s/n): ')).lower()
print('Fim do programa!')

