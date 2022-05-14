km = int(input('\033[35mQuantos km o carro percorreu? '))
d = int(input('\033[33mPor quantos dias o carro foi alugado? '))
s = 0.15*km + 60*d
print(f'\033[36mO valor a ser pago pelo aluguel do carro é de {s}\033[m')