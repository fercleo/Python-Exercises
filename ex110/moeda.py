def metade(mtd=0, format=False):
    mtd /= 2
    return mtd if format is False else moeda(mtd)


def dobro(dob=0):
    dob *= 2
    return dob if format is False else moeda(dob)


def aumentar(aum=0):
    aum *= 1.20
    return aum if format is False else moeda(aum)


def diminuir(dim=0):
    dim *= 0.80
    return dim if format is False else moeda(dim)


def moeda(preço=0, moeda = 'R$' ):
    return(f'{moeda}{preço:.2f}').replace('.',',')

def resumo(preço=0, taxaa=20, redução=20):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Metade: \t{metade(preço)}')
    print(f'Dobro: \t{dobro(preço)}')
    print(f'Aumento de \t{taxaa}%: \t{aumentar(preço)}')
    print(f'Redução de \t{redução}% \t{diminuir(preço)}')