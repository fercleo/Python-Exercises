lista = []
lista1 = []
lista2 = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    c = str(input('Deseja continuar? [s/n] '))
    if n % 2 == 0:
        lista1.append(n)
    elif n % 2 != 0:
        lista2.append(n)
    if c in 'Ss':
        continue
    else:
        break
print(f'Os números lidos foram {lista}.')
print(f'Os números pares são {lista1}.')
print(f'Os números ímpares são {lista2}.')
