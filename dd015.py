menor = 0
adulto = 0
idoso = 0

for c in range(0, 8):
    idade = int(input('Qual a sua idade? '))
    if idade < 18:
        menor += 1
    elif idade < 60:
        adulto += 1
    else:
        idoso += 1
print(f'O total de menores é {menor}')        
print(f'O total de adultos é {adulto}')
print(f'O total de idosos é {idoso}')
print('Fim do programa!')        
    