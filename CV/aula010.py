'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito!')
else:
    print('Seu nome é muito comum!')
print('Bom dia, {}'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média final foi {:.1f}'.format(m))
print('Parabéns!' if m>=7 else 'Estude Mais!')
#condição simplificada