somaidade = 0
medidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'---{p}ª Pessoa ---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

medidade = somaidade / 4
print(f'A média de idade é {medidade}')
print(f'O Homem mais velho tem {maioridadehomem} ano e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} Mulheres com menos de 20 anos')

