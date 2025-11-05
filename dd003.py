nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))
if idade <= 12:
    print('Você é uma criança!')
elif idade <= 17:
    print('Você é um adolecente!')
elif idade <= 59:
    print('Você é um adulto!')
else:
    print('Você é idoso!')
print('Seja bem vindo e tenha um bom dia, {}!'.format(nome))
