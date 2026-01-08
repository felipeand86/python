titulo = 'Banco SG'
print('='*30)
print(titulo.center(30))
print('='*30)
dindin = 50
totdindin = 0
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
while True:
    if total >= dindin:
        total -= dindin
        totdindin += 1
    else:
        if totdindin > 0:
            print(f'Total de {totdindin} cedulas de R${dindin}')
        if dindin == 50:
            dindin = 20
        elif dindin == 20:
            dindin = 10
        elif dindin == 10:
            dindin = 1
        totdindin = 0
        if total == 0:
            break
print('Bom vindo ao banco sem grana, volte sempre!')
