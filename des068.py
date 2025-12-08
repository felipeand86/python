from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo =  str(input('Qual sua escolha? [Par/Impar]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, e o total deu {total}')
    print(f'Par' if total %2 == 0 else 'Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu.')
            v += 1
        else:
            print('Você perdeu.')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu.')
            v += 1
        else:
            print('Você perdeu.')
            break
    print(f'Vamos jogar novamente..')
print(f'Fim de jogo, você venceu {v} vezes')
