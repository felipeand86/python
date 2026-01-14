palavras = ('aprender', 'programar', 'linguagem', 'curso', 'gratuito', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')
