'''def mostrarlinha():
    print('=-'*30)

#Programa principal
mostrarlinha()
print('   Hello')
mostrarlinha()
mostrarlinha()
print('   Função')
mostrarlinha()
mostrarlinha()
print('   Python')
mostrarlinha()


def tit(txt):
    print('-='*30)
    print(txt)
    print('=-'*30)

tit(' Python')
tit(' Funções')
tit(' Rotina')


#Criando a definição de função
def soma(a, b):
    print(f' A = {a} + B = {b}')
    s = a + b
    print(f'A soma entre A + B é = {s}')

#Programa principal
soma(2, 4)
soma(3, 9)
soma(1, 5)
soma(2, 4)



#definição de função
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

#Programa principal
contador(2, 3, 4)
contador(8,9)
contador(2, 5, 8, 7)
'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

val = [7,5,2,9,1]
dobra(val)
print(val)



