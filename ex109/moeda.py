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