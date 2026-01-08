print('\33[33m-=\33[m' * 20)
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario? '))
anos = int(input('Em quantos anos deseja pagar? '))
print('\33[34m=-\33[m' * 20)
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Com o salario de R${:.2f} para comprar a casa de R${:.2f},'.format(salario, casa, end=''))
print('terá que pagar R${:.2f} por mês!'.format(prestacao))
if prestacao <= minimo:
    print('\33[34mEmprestimo pode ser concedido!\33[m')
else:
    print('\33[31mEmprestimo não pode ser concedido!\33[m')
