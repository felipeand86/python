soma = cont = num = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Digitou {cont} e a soma entre eles é {soma}')
