v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
maior = v1 or v2
if v1 > v2:
    print('{} é maior que {}'.format(maior, v1))
if v2 > v1:
    print('{} é maior que {}'.format(maior, v2))
elif v1 == v2:
    print('Não existe valor maior, os dois são iguais {} e {}'.format(v1, v2))
