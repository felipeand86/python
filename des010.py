real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.45
euro = real / 6.36
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar E${:.2f}'.format(real, euro))
# Desafio 010 - Conversor de Moedas
