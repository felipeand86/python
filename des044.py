print('{:=^40}'.format(' Lojas Cem Dinheiro '))

valor = float(input('Qual o valor das compras? R$ '))
print('''Escolha uma das opções: 
      [ 1 ] à vista em dinheiro ou pix
      [ 2 ] à vista no cartão de débito
      [ 3 ] 2x no cartão de crédito
      [ 4 ] 3x ou mais no cartão de crédito''')
opcao = int(input('Qual opção? '))
if opcao == 1:
    pgto = valor - (valor * 10 / 100)
    print(f'O valor à vista no pix tem desconto de 10%, então de R${valor:.2f} vai custar R${pgto:.2f}')
elif opcao == 2:
    pgto = valor - (valor * 5 / 100)
    print(f'O valor à vista no cartão de débito tem desconto de 5%, então de {valor:.2f} vai custar R${pgto:.2f}')
elif opcao == 3:
    pgto = valor / 2
    print(f'Parcelado em 2x no cartão de crédito, vai ficar 2x de R${pgto:.2f}')
elif opcao == 4:
    pgto = valor + (valor * 20 / 100)
    vezes = int(input('Deseja parcelar em quantas vezes? '))
    parc = pgto / vezes
    print(f'O valor parcelado em 3x ou mais, o juros é de 20%')
    print(f'Total a ser pago R${pgto:.2f} parcelado em {vezes}x de R${parc:.2f}')
else:
    print('\33[31mOpção inválida, tente novamente inserindo o valor!\33[m')

