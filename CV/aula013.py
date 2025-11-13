'''
for c in range(0, 5):
    print('Olá')
print('Fim')
'''

ini = int(input('Digite o numero inicial: '))
fim = int(input('Digite o numero final: '))
passo = int(input('Digite o numero passo: '))
for c in range(ini, fim + 1, passo):
    print(c)
print('Fim da leitura!')
