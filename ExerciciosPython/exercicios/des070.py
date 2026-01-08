total = totmil = menor = cont = 0
barato = ''
while True:
    nomeprod = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nomeprod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Tem {totmil} produtos custando mais de R$1.000 reais')
print(f'O produto mais barato {barato} que custa R${menor:.2f}')
