
print('=' * 40)
print('Gerenciamento de pagamentos')
print('=' * 40)
valor = float(input('Qual o preço das compras? R$ '))

print('''formas de pagamento:
[ 1 ] à vista dinheiro / Pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais''')

opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print(f'o valor total dos produtos é {valor:.2f} com o desconto de 10% você irá pagar {total:.2f}')
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print(f'o valor total dos produtos é {valor:.2f} com o desconto de 5% você irá pagar {total:.2f}')
elif opcao == 3:
    total = valor
    parc = total / 2
    print(f'{valor:.2f} parcelado sem juros, o valor total é de 2x de {parc:.2f}')
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    vezes = int(input('Em quantas vezes deseja pagar? '))
    parc = total / vezes
    print(f'sua compra de {valor:.2f} vai custar {total:.2f} parcelado em {vezes}x de R$ {parc:.2f}')
else:
    total = 0
    print('\33[31mOpção invalida, tente novamente!\33[m')






