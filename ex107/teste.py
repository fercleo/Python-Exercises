from ex107 import moeda

p = float(input('Digite um valor: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Adicionando 20% a {p} temos {moeda.aumentar(p)}')
print(f'Reduzindo 20% de {p} temos {moeda.diminuir(p)}')
