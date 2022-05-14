v1 = int(input('Digite um número: '))
v2 = int(input('Digite um segundo número: '))
v3 = int(input('Digite um terceiro número: '))
v4 = int(input('Digite um quarto número: '))
vtotal = (v1, v2, v3, v4)
if vtotal.count(9) == 1:
    print(f'O número 9 apareceu {vtotal.count(9)} vez.')
elif vtotal.count(9) == 0:
    print('O número 9 não foi digitado')
else:
    print(f'O número 9 apareceu {vtotal.count(9)} vezes.')
if 3 in vtotal:
    print(f'O primeiro número 3 foi digitado na {vtotal.index(3) + 1}ª posição.')
else:
    print('Não há número 3 nos valores digitados.')
    print('Os valores pares digitados foram: ', end='')
    for p in vtotal:
        if p % 2 == 0:
            print(p, end=', ')

