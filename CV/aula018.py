
#lista composta, uma lista dentro de outra lista
'''pessoas = [['Felipe', 39], ['Ana', 37], ['Daniel', 45],['Amanda', 30], ['Enzo', 12]]
print(pessoas[4][0])'''

#lista composta organizada
'''pessoas = [['Felipe', 39], ['Ana', 37], ['Daniel', 45],['Amanda', 30], ['Enzo', 12]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

#lista com cópia
pessoas = list()
dado = list()
totma = totme = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:]) #Se caso esquecer de fazer a cópia com [:] a lista dado e pessoas criam ligação
    dado.clear()

for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} de {p[1]} é maior de idade!')
        totma += 1
    else:
        print(f'{p[0]} de {p[1]} é menor de idade!')
        totme += 1
print(f'Total de pessoas maiores de idade {totma}')
print(f'Total de pessoas menores de idade {totme}')

