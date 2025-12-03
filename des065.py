soma = quant = menor = maior = media = 0
continua = 's'
while continua in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / quant
print(f'Foram digitados {quant} números, e a média entre eles é de {media}')
print(f'O maior valor digitado foi {maior} e o menor {menor}')
