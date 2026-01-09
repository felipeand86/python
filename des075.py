num = (int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))
print(f'Você digitou os numeros {num}')
print(f'O numero nove foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O numero três foi digitado na posição {num.index(3)+1}ª')
else:
    print('O numero três não foi digitado em nenhum posição!')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' e ')
