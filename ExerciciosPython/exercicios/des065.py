soma = quant = media = maior = menor = 0
continua = 's'
while continua in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print(f'Foi digitado {quant} numeros e a média entre eles é {media}')
print(f'O maior numero digitado foi {maior} e o menor {menor}')
