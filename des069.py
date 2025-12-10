tot18 = totm20 = toth = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    if sexo == 'M':
        toth += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de {tot18} pessoas maiores de idade')
print(f'Total de {totm20} Mulheres com menos de 20 anos')
print(f'Total de {toth} Homens')
