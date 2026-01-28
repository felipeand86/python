from time import sleep
from random import randint
lista = list()
print('-='*30)
print('                   Jogo da Mega Sena          ')
print('-='*30)
jogos = list()
quant = int(input('Quantos jogos você quer gerar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*5, f' <<Sorteando {quant} jogos>> ', '-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

