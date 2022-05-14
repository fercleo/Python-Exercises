l = float(input('Qual a largura da parede? (metros)'))
alt = float(input('Qual a altura de parede? (metros)'))
area = l*alt
tinta = area/2
print(f'A parede tem a dimensão de {l}x{alt} e a área é de {area}m². \n Portanto, serão necessários {tinta} litros de tinta para pintá-la.')