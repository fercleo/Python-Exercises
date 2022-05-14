frase = input('Digite uma frase: ').upper().replace(" ", "")
if frase == frase[::-1]:
    print('A frase é um palíndromo.')
else:
    print(f'A frase não é um palíndromo. O inverso de {frase} é {frase[::-1]}')