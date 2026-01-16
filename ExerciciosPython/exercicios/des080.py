sequencia = list()
for c in range(5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > sequencia[-1]:
        sequencia.append(n)
        print('Numero adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(sequencia):
            if n <= sequencia[pos]:
                sequencia.insert(pos, n)
                print(f'Numero adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Ordem dos numeros: {sequencia}')

