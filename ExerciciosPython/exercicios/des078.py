num = []
maior = menor = 0
for i in range(5):
    num.append(int(input(f'Digite um numero na posição {i}: ')))
    if i == 0:
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
print(f'O maior valor foi {maior} digitado nas posições: ')
for c, v in enumerate(num):
    if v == maior:
        print(f'{c}... ', end='')
print()
print(f'O menor valor foi {menor} digitado nas posições: ')
for c, v in enumerate(num):
    if v == menor:
        print(f'{c}... ', end='')
print()
