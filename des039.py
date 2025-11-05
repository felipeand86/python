from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu no ano de {} tem {} anos no ano de {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento vai acontecer no ano de {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('O seu alistamento aconteceu há {} anos.'.format(saldo))
    ano = atual - saldo 
    print('Você deveria ter se alistado no ano de {}.'.format(ano))
