nome = str(input('Digite seu nome: '))
if nome == 'Felipe':
    print('Que nome bonito!')
elif nome in 'Júlia Cláudia Maria':
    print('Seu nome não é mais tão comum assim')
elif nome == 'Pedro' or 'João' or 'Valentina' or 'Enzo':
    print('Seu nome é meio raiz e meio nutella')
print('Bom dia {}!'.format(nome))