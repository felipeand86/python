from random import randint
from time import sleep
while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')
    try:
        jogador = int(input('Qual é a sua jogada? '))
        if jogador not in [0 , 1 , 2]:
            print('Jogada inválida, tente novamente.')
            continue #volta par o inicio do while
    except ValueError:
        print('Por favor, digite (0, 1 ou 2)')
        continue
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('Pô')
    sleep(1)
    print('-=' * 15)
    print(f'O computador escolheu {itens[computador]}')
    print(f'O jogador escolheu {itens[jogador]}')
    print('-=' * 15)
    if computador == 0: #computador jogou pedra
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('Jogador vence')
        else:
            print('Computador vence')
    elif computador == 1: #computador jogou papel
        if jogador == 0:
            print('Computador vence')
        elif jogador == 1:
            print('Empate')
        else:
            print('Jogador vence')
    elif computador == 2: #computador jogou tesoura
        if jogador == 0:
            print('Jogador vence')
        elif jogador == 1:
            print('Computador vence')
        else:
            print('Empate!')
    print('-=' * 15)
    continuar = input('Deseja continuar? [s/n]')
    if continuar == 'n':
        print('Encerrando o jogo...', end='')
        print('Até a próxima!')
        break

