num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1,11):
    print(f'\033[34m{num}x{c} = {num*c}.')