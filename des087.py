matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somatc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end='')
        if matriz [l][c] % 2 == 0:
            somap = matriz [l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {somap}')
for l in range(0, 3):
    somatc += matriz [l][2]
print(f'A soma da terceira coluna é de {somatc}')
for c in range(0, 3):
    if maior == 0:
        maior = matriz [1][l]
    elif matriz [1][l] > maior:
        maior = matriz [1][l]
print(f'E o maior numero da segunda linha é {maior}')
