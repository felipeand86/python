num = int(input('Digite um número: '))
for c in range(1, 11):
    resultado = num * c
    if resultado %2 == 0:
        print(f'{num} x {c} = {resultado}')
print('Fim do programa!')        


    
