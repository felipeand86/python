from math import hypot
co = float(input('Qual é o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente? '))
#hipot = (co ** 2 + ca ** 2) ** (1/2) # calculo manual
hipot = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hipot))
