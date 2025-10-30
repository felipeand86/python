print('\33[34m-=\33[m' * 20)
print('\33[33mAnalisador de Triângulos\33[m')
print('\33[34m-=\33[m' * 20)
r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores digitador \33[34mPODEM\33[m formar um triângulo!')
else:
    print('Os valores digitados \33[31mNÃO PODEM\33[m formar um triângulo!')
