amarelo = '\33[33m'
azul = '\33[34m'
vermelho = '\33[31m'
reset = '\33[m'

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
print(f'Valor do imc: {imc:.2f}')
if imc <= 18.5:
    print(f'{amarelo}Abaixo do peso{reset}')
elif imc <= 24.9:
    print(f'{azul}Normal{reset}')
elif imc <= 29.9:
    print(f'{amarelo}Está acima do peso{reset}')
else:
    print(f'{vermelho}Obesidade{reset}')
