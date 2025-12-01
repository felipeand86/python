primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}-> ', end='')
        termo += razao
        cont += 1
    print(' Pausa')
    mais = int(input('Quer mostrar mais algum termo? '))
print(f'Encerrando com {total} termos mostrados!')
