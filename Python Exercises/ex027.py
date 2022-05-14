nome = str(input('Digite seu nome completo: ')).strip()
divisao = nome.split()
print(f'\033[34mSeu primeiro nome é {divisao[0]} e seu último nome é: {divisao[-1]}')