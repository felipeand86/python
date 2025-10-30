salario = float(input('Qual o valor do salario? R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f} passa a ganhar R${:.2f}'.format(salario, aumento))    
