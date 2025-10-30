salario = float(input('Qual o valor do salario? '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganhava o salario R${:.2f} passa a ganhar R${:.2f}'.format(salario, aumento))
