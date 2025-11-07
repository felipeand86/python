usuario_correto = 'admin'
senha_correta = '1234'

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    usuario = str(input('Usuário: '))
    senha = (input('Senha: '))

    if usuario == usuario_correto and senha == senha_correta:
        print('Acesso permitido!')
        break
    else:
        tentativas += 1
        print('Usuário ou senha incorretos!')
        print(f'Tentativa {tentativas} de {max_tentativas}\n')
if tentativas == max_tentativas:
    print('Conta bloqueada!')


'''
usuario_correto = 'admin'
senha_correta = '1234'

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    if usuario == usuario_correto and senha == senha_correta:
        print('Acesso permitido! ✅')
        break  # sai do loop imediatamente
    else:
        tentativas += 1
        print('Usuário ou senha incorretos!')
        print(f'Tentativa {tentativas} de {max_tentativas}\n')

if tentativas == max_tentativas:
    print('Conta bloqueada! 🚫')
'''