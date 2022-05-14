def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: Opcional (mostrar conta)
    :return: Valor fatorial do número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end= '')
            if c > 1:
                print(' x ', end= '')
            else:
                print(' = ', end= '')
        f *= c
    return f


#programa principal
print(fatorial(5, show=True))