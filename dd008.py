idade = int(input('Qual a idade do nadador? '))
if idade <= 7:
    print('Infantil (A)')
elif idade <= 11:
    print('Infantil (B)')
elif idade <= 13:
    print('Juvenil (A)')
elif idade <= 17:
    print('Juvenil (B)')
else:
    print('Categoria adulto')
print(f'O nadador tem {idade} anos')
   