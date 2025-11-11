from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Sua categoria é Mirim!')
elif idade <= 14:
    print('Sua categoria é Infantil!')
elif idade <= 19:
    print('Sua categoria é Junior!')
elif idade <= 25:
    print('Sua categoria é Sênior!')
else:
    print('Sua categoria é Master!')
