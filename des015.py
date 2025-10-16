dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
dias_alugado = (dias * 60) + (km * 0.15)
print('O valor total a ser peago é de: R${:.2f}'.format(dias_alugado))
# Desafio 015 - Aluguel de Carro
