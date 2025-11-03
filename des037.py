num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das opções: 
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} converter para binário é igual a {}'.format(num, bin(num) [2:]))
elif opcao == 2:
    print('{} converter para octal é igual a {}'.format(num, oct(num) [2:]))
elif opcao == 3:
    print('{} converter para hexadecimal é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Escolha inválida, tente novamente!')