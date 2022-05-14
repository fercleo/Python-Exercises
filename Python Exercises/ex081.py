lista = []
n1 = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    c = str(input('Deseja continuar? [s/n] '))
    if c in 'Ss':
        continue
    else:
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse = True)
print(f'A lista dos números digitados em ordem decrescente é: {lista} ')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não está na lista.')