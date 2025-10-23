from random import randint
#faz o comp randomizar
comp = randint(0,5)
print('*-=-*' * 10)
print('Tente adivinhar o numero que estou pensando de 0 a 5: ')
print('*-=-*' * 10)
#o jogador tenta adivinhar
jog = int(input('Escolha um numero entre 0 e 5: '))
if jog == comp:
    print('Parabéns, você me venceu!')
else:
    print('Não foi dessa vez, pensei no numero {} e não no {}'.format(comp, jog))

