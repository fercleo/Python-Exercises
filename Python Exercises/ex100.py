from time import sleep
from random import randint
def sorteia(numeros):
    print('Sorteando 5 valores da lista:')
    for c in range(0,5):
        n = randint(1,10)
        numeros.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')


def somapar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')
numeros = []
sorteia(numeros)
somapar(numeros)


