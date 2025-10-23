vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('Multado! você está a {}km/h que é acima do limite permitido.'.format(vel))
    multa = (vel - 80) * 7
    print('Sua multa é de R${}'.format(multa))
print('Boa viagem!')  
  