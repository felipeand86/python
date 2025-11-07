inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('passo: '))
cont = inicio
while cont <= fim:
    print(cont)
    cont += passo
    if passo == 0:
        passo = 1
print('Fim do programa!')    

