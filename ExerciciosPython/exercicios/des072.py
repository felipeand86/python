cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou o numero {cont[num]}')
continuar = ''
while continuar in 'Ss':
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar != 'N':
        num = int(input('Digite um numero entre 0 a 20: '))
        print(f'Você digitou o numero {cont[num]}')
    else:
        print('Encerrando o programa.')

