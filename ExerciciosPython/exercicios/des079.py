num = []
while True:
    n = int(input('Digite um numero: '))
    if n not in num:
        num.append(n)
        print('Numero adicionado!')
    else:
        print('Não adiciono numero repetido!')
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
num.sort()
print(f'Os numeros foram: {num}')
