from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1, 8):
    nasc = int(input(f'Em que ano a {pes}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade <= 21:
        totmenor += 1
    else:
        totmaior += 1
print(f'Tivemos um total de {totmenor} menores de idade \nTivemos um total de {totmaior} maiores de idade.')

