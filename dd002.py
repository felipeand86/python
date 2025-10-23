def remove_vogais(s):
    vogais = "aeiouáAEIOUÁ"
    return "".join([c for c in s if c not in vogais])

s = input("Digite uma string: ")
print(remove_vogais(s))