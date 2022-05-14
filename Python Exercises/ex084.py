temp= []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(float(input('Digite o peso da pessoa: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    pergunta = str(input('Gostaria de cadastrar outra pessoa? [s/n] ')).strip()
    if pergunta in 'Nn':
        break
print(f'Foi/Foram cadastrada(s) {len(princ)} pessoa(s).')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0] }]', end='')
print()