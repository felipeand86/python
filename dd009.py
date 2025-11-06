usuario = str(input('Usuário: '))
senha = int(input('Senha: '))
if usuario == 'admin' and senha == 1234:
    print(f'Login bem-sucedido, bem vindo {usuario}!')
else:
    print('Usuário ou senha inválidos!')

    