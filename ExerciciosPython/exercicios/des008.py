medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
print('A medida de {}m corresponde a {:.1f}hm e {:.1f}km'.format(medida, hm, km))
# Desafio 008 - Conversor de Medidas
