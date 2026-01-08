n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'A média entre as notas {n1:.1f} e {n2:.1f} é {m:.1f}')
if m >= 7:
    print('Aprovado!')
elif m >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')

