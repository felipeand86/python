casa = float(input('Qual é o valor do imovel? R$'))
salario = float(input('Qual é o salario? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('O emprestimo pode ser concedido!')
else: 
    print('O emprestimo foi negado!')
    