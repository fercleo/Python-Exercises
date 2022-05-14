extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número de 1 a 20 para ver sua escrita por extenso: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end= '')
print(f'Você digitou o número {extenso[numero]}.')
