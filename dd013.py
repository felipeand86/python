soma = 0
num = 1

while num != 0:
    num = int(input('Digite um número (0 para sair): '))
    if num > 0:
        soma += num
    elif num < 0:
        print('Número negativo não será somado!')
print(f'A soma dos números positivos é {soma}.')     
   