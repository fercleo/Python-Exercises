print('\033[34m*-*' * 21)
print('Soma entre todos os números ímpares no intervalo de 1 até 500:')
print('*-*' * 21)
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma resulta em {soma}')