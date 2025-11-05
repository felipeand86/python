from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu no ano de {} tem {} anos de idade no ano de {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Seu alistamento já aconteceu há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu ano de alistamento foi em {}'.format(ano))


