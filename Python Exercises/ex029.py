velocidade = int(input('Qual a velocidade do veículo em km/h? '))
if velocidade <= 80:
   print('O veículo está dentro dos limites de velocidade.')
else:
    multa = 7*(velocidade-80)
    print(f'O veículo foi multado. O valor da multa é de: {multa}R$.')
