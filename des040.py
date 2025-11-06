#media informa reprovado, aprovado ou recuperação
n1 = float(input('Primeiro nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('\33[34mAprovado!\33[m')
elif m >= 5:
    print('\33[33mRecuperação!\33[m')
else:
    print('\33[31mReprovado!\33[m')
print(f'A média entre as duas notas é de {m:.1f}')
    