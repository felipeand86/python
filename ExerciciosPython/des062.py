print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}-> ', end='')
        termo += razao
        cont += 1
    print(' Pausa')
    mais = int(input('Quer mais mais algum termo? '))
print(' Fim')
