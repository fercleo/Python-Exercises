lst = [] #Maior e menor de uma lista
for c in range (1,6):
    peso = (float(input(f'Qual  o peso da {c} pessoa? ')))
    lst += [peso]
print(f'O maior peso foi: {max(lst)}.')
print (f'O menor peso foi: {min(lst)}.')