n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = input('Escolha a operação (+, -, *, /): ')
if op == '+':
    res = n1 + n2
elif op == '-':
    res = n1 - n2
elif op == '*':
    res = n1 * n2
elif op == '/':
    if n2 == 0:
        print('Erro: divisão por zero não é permitida!')
    else:
        res = n1 / n2
        print(f'O resultado é: {res}')
else:
    print('Entrada inválida.')
print(f'O resultado entre os valores é: {res} ')
