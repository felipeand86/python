from random import randint
computador = randint(0, 5)
print('=*=' * 20)
print('Tente adivinhar o numero que estou pensando: ')
print('=*=' * 20)
jogador = int(input('Escolha um numero entre 0 e 5: '))
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou, pensei no numero {} e não no {}'.format(computador, jogador))
    