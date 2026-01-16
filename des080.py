lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > len(lista):
        lista.append(n)
        print('O numero foi adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O numero foi adicionado na posição {pos}')
                break
            pos += 1
print(f'Os numeros da lista ficaram assim: {lista}')

