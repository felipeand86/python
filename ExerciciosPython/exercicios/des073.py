times = 'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Chapecoense', 'BotaFogo', 'Bahia', 'São Paulo', 'Grêmio'
print('=-'*25)
print(times)
print('=-'*25)
print(times[0:4])
print('=-'*25)
print(times[-4:])
print('=-'*25)
print(sorted(times)) #ordem alfabetica
print('=-'*25)
print(f'O time Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print(len(times))
print(times.count('Cruzeiro'))
for t in times:
    print(t)
