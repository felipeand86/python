from random import randint
from time import sleep

vermelho = '\33[31m'
verde = '\33[32m'
amarelo = '\33[33m'
reset = '\33[m'

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''Suas opções?
          [ 1 ] Pedra
          [ 2 ] Papel
          [ 3 ] Tesoura''')
    try:
        jogador = int(input('Qual a sua jogada? '))
        if jogador not in [0, 1, 2]:
            print('Jogada inválida, tente novamente!')
            continue
    except ValueError:
        print('Por favor, digite 0, 1 ou 2')
        continue
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Po!')
    sleep(1)
    print('-=' * 15)
    print(f'O computador escolheu {itens[computador]}')
    print(f'O jogador escolheu {itens[jogador]}')
    print('-=' * 15)
    if computador == 0: #computador escolhe Pedra
        if jogador == 0:
            print(f'{amarelo}Empate{reset}')
        elif jogador == 1:
            print(f'{verde}Vitória{reset}')
        else:
            print(f'{vermelho}Derrota{reset}')
    if computador == 1: #computador escolhe Papel
        if jogador == 0:
            print(f'{vermelho}Derrota{reset}')
        elif jogador == 1:
            print(f'{amarelo}Empate{reset}')
        else:
            print(f'{verde}Vitória{reset}')
    if computador == 2: #computador escolhe Tesoura
        if jogador == 0:
            print(f'{verde}Vitória{reset}')
        elif jogador == 1:
            print(f'{vermelho}Derrota{reset}')
        else:
            print(f'{amarelo}Empate{reset}')
    print('-=' * 15)            
    continuar = input('Deseja continuar? [s/n]')
    if continuar != 's':
        print('Encerrando o jogo.. até a próxima!')
        break

