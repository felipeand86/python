'''
import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
'''

from math import tan, sin, cos, radians
angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o \33[34mseno de {:.2f}\33[m'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o \33[33mcosseno de {:.2f}\33[m'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a \33[31mtangente de {:.2f}\33[m'.format(angulo, tangente))


