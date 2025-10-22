frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A letra A aparece pala primeira vez na posição {}'.format(frase.upper().find('A') + 1))
print('A letra A aparece pela última vez na posição {}'.format(frase.upper().rfind('A') + 1))
# Desafio 026 - Primeira e última ocorrência de uma string
