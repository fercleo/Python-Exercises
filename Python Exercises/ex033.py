a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor é {maior} e o menor é {menor}.')