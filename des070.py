total = totmil = menor = cont = 0
barato = ''
rodape = '===Fim do Programa==='
while True:
    nomeprod = str(input('Nome do produto: ')).strip().upper()
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
print(rodape.center(25))
print(f'O total da compra foi R${total}')
print(f'Teve {totmil} produtos que custaram mais de R$1.000 reais')
print(f'O nome do produto mais barato foi {barato}')

