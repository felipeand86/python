num = []
for i in range(5):
    n = int(input('Digite um numero: '))
    num.append(n)
print(f'Você digitou {num} numeros')
print(f'O maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')
for c, v in enumerate(num):
    print(f'O valor {v} está na posição {c}')