lista = [[], []]
valor = 0
for v in range(1, 8):
    valor = int(input(f'Digite o {v}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 != 0:
        lista[1].append(valor)
lista[0].sort()
print(f'Os números pares são {lista[0]}.')
lista[1].sort()
print(f'Os número ímpares são {lista[1]}.')