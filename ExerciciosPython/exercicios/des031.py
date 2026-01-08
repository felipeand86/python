distancia = float(input('Qual a distancia da viagem em km? '))
print('A distancia da viagem vai ser de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('A viagem vai te custar R${}'.format(preço))
