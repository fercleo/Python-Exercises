print('*-*' * 9)
print('Analisando Triângulos v2.0')
print('*-*' * 9)
segum = float(input('Primeiro segmento: '))
segdois = float(input('Segundo segmento: '))
segtres = float(input('Terceiro segmento: '))
if segum == segdois and segum == segtres:
    print('\033[32mOs segmentos acima podem formar um triângulo equilátero.')
elif segum == segdois or segum == segtres or segtres==segdois:
    print('\033[32mOs segmentos acima podem formar um triângulo isósceles.')
elif segum < segdois + segtres and segdois < segum + segtres and segtres < segum + segdois:
    print('\033[32mOs segmentos acima podem formar um triângulo escaleno.')
else:
    print('\033[31mOs segmentos acima não podem formar um triângulo.')
