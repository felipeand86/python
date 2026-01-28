pessoas = list()
dado = list()
totpes = totlev = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

for p in pessoas:
    if p[1] >= 99:
        print(f'{p[0]} com o peso {p[1]} está acima do peso!')
        totpes += 1
    else:
        print(f'{p[0]} com o pesso {p[1]} está com o peso normal')
        totlev += 1
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'Tem {totpes} pessoas acima do peso e {totlev} pesspas com o peso normal ')


