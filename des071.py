valor = int(input('Qual valor deseja sacar? R$'))
total = valor
din = 50
totdin = 0
while True:
    if total >= din:
        total -= din
        totdin += 1
    else:
        if totdin > 0:
            print(f'Total de {totdin} notas de R${din}')
        if din == 50:
            din = 20
        elif din == 20:
            din = 10
        elif din == 10:
            din = 1
        totdin = 0
        if total == 0:
            break
