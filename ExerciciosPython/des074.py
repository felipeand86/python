from random import randint
maior = menor = 0
num = randint(0, 5)
print(f'Os valores sorteados foram {num},{num},{num},{num}')
if num > maior:
    num = maior
else:
    num = menor
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
