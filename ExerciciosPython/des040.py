n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Parabéns, aprovado!')
elif media >= 5 and media < 7:
    print('Você deverá fazer recuperação!')
else:
    print('Reprovado!')
print('Sua média foi de {}'.format(media))