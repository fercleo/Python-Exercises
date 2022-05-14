listanum = []
while True:
    v = int(input('Digite um valor: '))
    c = str(input('Deseja continuar? [s/n] '))
    if v not in listanum:
        listanum.append(v)
        print('Valor adicionado com sucesso.')
    else:
        print('Este valor já foi adicionado, será desconsiderado.')
    if c in 'Ss':
        continue
    else:
        break
listanum.sort()
print(f'Seus valores adicionados foram {listanum}.')
