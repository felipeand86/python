vel = float(input('Qual a velodidade do carro? '))
if vel > 80:
    print('Multado! você está a {}km/h que é acima do limite!'.format(vel))
    multa = (vel - 80) * 7
    print('Sua multa é de R${:.2f}'.format(multa))
print('Boa viagem!')