num = int(input('Digite qualquer numero de 0 a 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('O numero a ser analisado: {}'.format(num))
print('Milhares: {}'.format(m))
print('Centenas: {}'.format(c))
print('Dezenas: {}'.format(d))
print('Unidades: {}'. format(u))
# Desafio 023 - Separando dígitos de um número
