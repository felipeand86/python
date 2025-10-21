salario = float(input('Qual é o salario do funcionário? R$ '))
aumento = salario + (salario * 15 / 100)
print('O salario de R${:.2f} foi aumentado em 15% para R${:.2f}'.format(salario, aumento))
