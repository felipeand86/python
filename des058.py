from random import randint
computador = randint(0, 10)
print('Pensei em um numero, tente adivinhar em qual!')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Dê o seu palpite: '))
    palpite = palpite + 1
    if computador == jogador:
        acertou = True
    elif computador > jogador:
        print('Tente um numero maior!')
    else:
        print('Tente um numero menor!')
print(f'Parabéns, você acertou!.. Em {palpite} tentativas.')     
  