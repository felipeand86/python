time = list()
partidas = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas jogou o {jogador["nome"]}? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! DIgite apenas S ou N. ')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('--'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*30)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com esse código.')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["nome"]):
            print(f'   No jogo {i+1} fez {g} gols.')
print('Encerrando.')
