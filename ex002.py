numeros = []  # lista para guardar os números

print('Digite números (digite 0 para parar):')

# WHILE – repetição até o usuário parar
while True:
    n = int(input('Número: '))
    if n == 0:  # condição para sair
        break
    numeros.append(n)

print('\n--- MENU ---')
print('[1] Mostrar todos os números')
print('[2] Mostrar apenas números pares')
print('[3] Mostrar o maior número')
print('[4] Mostrar cada número elevado ao quadrado')
print('[5] Sair')

# WHILE – menu continua até escolher sair
while True:
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('\nVocê escolheu: Mostrar todos os números')
        for num in numeros:  # FOR para percorrer a lista
            print(num)

    elif opcao == 2:
        print('\nNúmeros pares:')
        for num in numeros:
            if num % 2 == 0:  # IF dentro do FOR
                print(num)

    elif opcao == 3:
        print(f'\nO maior número é: {max(numeros)}')

    elif opcao == 4:
        print('\nNúmeros elevados ao quadrado:')
        for num in numeros:
            print(f'{num} → {num ** 2}')

    elif opcao == 5:
        print('\nSaindo do programa...')
        break

    else:
        print('\nOpção inválida! Tente novamente.')
