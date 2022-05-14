def metade(mtd=0):
    mtd /= 2
    return mtd


def dobro(dob=0):
    dob *= 2
    return dob


def aumentar(aum=0):
    aum *= 1.20
    return aum


def diminuir(dim=0):
    dim *= 0.80
    return dim


def moeda(preço=0, moeda = 'R$' ):
    return(f'{moeda}{preço:.2f}').replace('.',',')