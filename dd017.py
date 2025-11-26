from random import randint
computador = randint(0, 10)
print('Estou pensando em um numero, adivinhe qual é.')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpite = palpite + 1
    if computador == jogador:
        acertou = True
    elif computador > jogador:
        print('Tente um numero maior.')
    else:
        print('Tente um numero menor')
print(f'Parabens, acertou em {palpite} tentativas.')        
