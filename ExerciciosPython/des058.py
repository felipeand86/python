from random import randint
computador = randint(0, 10)
print('Pensei em um número entre 0 a 10, tente adivinhar qual é: ')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Dê o seu palpite: '))
    palpite += 1
    if computador == jogador:
        acertou = True
    elif computador > jogador:
        print('Mais.. Tente novamente!')
    else:
        print('Menos.. Tente novamente!')
print(f'Voce acertou em {palpite} tentativas')

