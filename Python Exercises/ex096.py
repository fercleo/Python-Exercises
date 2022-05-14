def area(l, c):
     a = l * c
     print(f'A área de um terreno {l}x{c} é de {a}m².')


#programa principal
print('-=' * 20)
print(f'         CALCULADOR DE ÁREAS')
print('-=' * 20)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)
