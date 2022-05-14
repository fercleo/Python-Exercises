matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somatc = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] : '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print('*-*' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('*-*' * 20)
print(f'A soma dos números pares é {soma}.')
for l in range(0, 3):
    somatc += matriz[l][2]
print(f'A soma dos números da terceira coluna é {somatc}.')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}. ')