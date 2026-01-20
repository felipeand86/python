num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-'*25)
print(f'Numeros digitados {num}')
print(f'Numeros pares {par}')
print(f'Numeros impares {impar}')
