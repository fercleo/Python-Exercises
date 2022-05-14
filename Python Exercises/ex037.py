print('\033[36m-*-' * 10)
print('Conversor de Bases Numéricas')
print('-*-' * 10)
num = int(input('Digite um número inteiro: '))
choose = input('Escolha qual sera a base da conversão: \n [1] para binário \n [2] para octal \n [3] para hexadecimal: ')
if choose == '1':
    print(f'O numéro {num} em binário é {num:b}')
elif choose == '2':
    print(f' O número {num} em octal é {num:o}')
elif choose == '3':
    print(f' O número {num} em hexadecimal é {num:x}')
