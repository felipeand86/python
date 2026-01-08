nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome..')
print('Seu nome em MAÍUSCULA é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


'''nome2 = 'André Silva Felipe Smith'
print(nome2.lower())'''

'''nome3 = 'Arnold Swarzzenego Pit da Cruise'
print(len(nome3))'''

'''
nome4 = 'Curso de Python'
print(nome4.lower().find('python')) #nesse caso o lower().find('python') está olhando qual a pos inicia a palavra python
'''

