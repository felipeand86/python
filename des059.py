from time import sleep
opcao = 0
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    ''')
    print('-=' * 10)
    opcao = int(input('-> Qual a sua opção? '))
    print('-=' * 10)
    if opcao == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif opcao == 2:
        multi = num1 * num2
        print(f'{num1} x {num2} = {multi}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior entre os dois valores é {maior}')
    elif opcao == 4:
        print('-=' * 10)
        print('Digite os valores novamente.')
        print('-=' * 10)
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Encerrando o programa..')
        sleep(2)
    else:
        print('Opção inválida, tente novamente!')

