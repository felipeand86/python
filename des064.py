n = cont = soma = 0
n = int(input('Digite um numero: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero: '))
print(f'Você digitou {cont} numeros e a soma entre eles é {soma}')    
