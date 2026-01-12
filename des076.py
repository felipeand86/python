titulo = 'Listagem de Preços'
lista = ('Lápis', 1.20,
         'Borracha', 1.45,
         'Caderno', 14.80,
         'Compasso', 7.40,
         'Cola', 6.00,
         'Estojo', 5.50,
         'Mochila', 100,
         'Livro', 22.50)
print('-'* 40)
print(titulo.center(40, " "))
print('-'* 40)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>6.2f}')
print('='* 40)
