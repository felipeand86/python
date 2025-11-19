tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print(f'{c}', end =' ')    
print(f'\n\33[mO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('Por isso ele é um número primo')
else:
    print('Por isso ele não é um número primo')

