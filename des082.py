num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('='*25)
print(f'Os numeros digitados {num}')
print(f'Os numeros pares {par}')
print(f'Os numeros impares {impar}')

