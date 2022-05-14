numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
if numero1 > numero2:
    print('\033[34mO primeiro valor é maior.')
elif numero1 < numero2:
    print('\033[34mO segundo valor é maior.')
elif numero1 == numero2:
    print('\033[34mOs valores são iguais.')