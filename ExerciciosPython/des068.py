from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Qual sua escolha? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}, total de {total}')
    print('Par' if total % 2 == 0 else 'Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu.')
            v += 1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu.')
            v += 1
        else:
            print('Voce perdeu.')
            break
    print('Vamos jogar novamente')
print(f'game over, você venceu {v} vezes')
