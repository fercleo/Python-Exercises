def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! digite um número quebrado.\033[m)')
        except(KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


#programa principal
int = LeiaInt('Digite um número inteiro: ')
float = LeiaFloat('Digite um número real: ')
print(f'O valor digitado foi {int} e o real foi {float}.')
