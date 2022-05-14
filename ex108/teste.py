from ex108 import moeda

p = float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Adicionando 20% a {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p))}')
print(f'Reduzindo 20% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p))}')
