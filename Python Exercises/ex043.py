print('`-´' * 7)
print('Calculadora de IMC')
print('`-´' * 7)
altura = float(input('Qual a sua altura? Ex:(1.75): '))
peso = float(input('Qual o seu peso? '))
imc = peso/altura**2
if imc < 18.5:
    print('\033[31mVocê está abaixo do peso ideal. Consulte um nutricionista.')
elif imc < 25.0:
    print('\033[32mVocê está no peso ideal, parabéns! Continue cuidando da sua saúde.')
elif imc < 30.0:
    print('\033[33mVocê está com sobrepeso. Considere uma dieta.')
elif imc < 40.0:
    print('\033[37mVocê está num quadro de obesidade. Consulte um nutricionista.')
elif imc > 40.0:
    print('\033[31mVocê está num quadro de obesidade mórbida. Consulte um nutricionista o mais breve possível.')