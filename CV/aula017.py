#.append > insere dados na ultima posição da lista
#.insert > insere dados na posição definida pelo programador

#valores = []
#valores = list()

'''valores = [1, 9] #conchetes indica que é uma lista e não uma tupla
valores.append(2)
valores.append(5)
valores.append(7)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Fim da lista')'''

a = [2, 4, 6, 8]
b = a[:]
b[2] = 9
print(a)
print(b)

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
for c, v in enumerate(valores):
    print(f'O numero {v} está na posição {c}')
print('Fim da contagem')'''

'''num = [1, 6, 8, 9]
num.append(4)
num.insert(1, 7)
num.sort()
#num.pop()
if 6 in num:
    num.remove(6)
    print('Numero removido')
else:
    print('Não encontrei o numero')
print(num)
print(f'A lista contem {len(num)} numeros')'''