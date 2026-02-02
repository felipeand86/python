'''pessoas ={'nome': 'Felipe', 'sexo': 'M', 'idade': 39}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

pessoas ={'nome': 'Felipe', 'sexo': 'M', 'idade': 39}
print(pessoas.keys())

pessoas ={'nome': 'Felipe', 'sexo': 'M', 'idade': 39}
print(pessoas.values())

pessoas ={'nome': 'Felipe', 'sexo': 'M', 'idade': 39}
print(pessoas.items()) #o resultado mostra as listas e tuplas

pessoas ={'nome': 'Felipe', 'sexo': 'M', 'idade': 39}
for k, v in pessoas.items(): #k de keys e v de values, tuplas e listas usam o "enumerate(pessoas):"
    print(f'{k} = {v}')

pessoas ={'nome': 'Felipe', 'sexo': 'M', 'idade': 39}
pessoas['nome'] = 'Dede'#em dicionarios para alterar um registro, pode ser feito dessa forma
pessoas['peso'] = 90.2#para adicionar dados ao dicionario, pode ser feito dessa forma
for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])


estado = dict()
brasil = list()
for c in range(0 ,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())#no caso de dicionario não se pode usar o [:] para fazer a copia de uma lista
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()'''
