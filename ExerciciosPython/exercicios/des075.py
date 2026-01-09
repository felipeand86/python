num = (int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))
print(f'Os numeros digitados foram {num}')
print(f'O numero nove foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O numero três aparece na posição {num.index(3)+1}ª')
else:
    print(f'O numero três não foi digitado em nenhuma posição!')
print('E os numeros pares foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')