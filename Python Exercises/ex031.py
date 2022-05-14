viagem = float(input('Qual a distância da viagem em km? '))
if viagem <= 200:
    mais = 0.50*(viagem)
    print(f'A sua viagem irá custar R${mais:.2f}.')
else:
    menos = 0.45*(viagem)
    print(f'A sua viagem irá custar R${menos:.2f}.')
