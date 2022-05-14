numero = str(input('Digite um número de 0 a 9.999: '))
milhar = numero[-4:-3]
centenas = numero[-3:-2]
dezenas = numero[-2:-1]
unidades = numero[-1:]
print(f'Esse número tem \033[34m{unidades}\033[m unidades \n \033[35m{dezenas}\033[m dezenas \n \033[31m{centenas}\033[m centenas \n \033[36m{milhar}\033[m milhares')