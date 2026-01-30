aluno = list()
while True: 
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*25)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-'*30)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*25)
    opc = int(input('Quer ver a nota de qual aluno? [999 para sair]'))
    if opc == 999:
        break
    if opc <= len(aluno)-1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
print('    <Finalizando>    ')
