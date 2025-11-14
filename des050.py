s = 0
for c in range(0, 6):
    num = int(input('Digite um valor: '))
    s += num
    if num %2 == 1:
        print(s)
print(f'A soma entre os valores é: {s}')    
print('Fim')        
