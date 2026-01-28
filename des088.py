from random import sample
from time import sleep
quant = int(input('Quantos jogos quer gerar? '))
print('\nGerando jogos...\n')
for i in range(quant):
    jogo = sample(range(1, 61), 6)
    jogo.sort()
    sleep(1)
    print(f'Jogo {i+1}: {jogo}')

