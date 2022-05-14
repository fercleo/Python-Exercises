print('\033[34m*-*' * 15)
print('Somador de todos os números pares digitados')
print('*-*' * 15)
soma = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos número pares informados é igual a {soma}.')

