lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-'*30)
print(f'Você digitou {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Os numeros na ordem decrecente são {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista!')
else:
    print('O numero 5 não faz parte da lista!')

