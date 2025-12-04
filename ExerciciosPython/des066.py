soma = cont = 0
while True:
    num = int(input('Digite um numero: [Para sair 999]'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foi digitado {cont} e a soma entre eles é {soma}')
