preço = float(input('Qual o valor do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto custa R${:.2f} e está com 5% de desconto, seu valor é de R${:.2f}'.format(preço, novo))
