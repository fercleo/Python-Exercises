vcasa = float(input('Qual o valor da casa em R$? '))
salario = float(input('Qual seu salário em R$? '))
tempo = float(input('Em quantos anos pretende pagar? '))
prestação = vcasa/(tempo*12)
if prestação<0.3*salario:
    print(f'\033[32mPara pagar uma casa de R${vcasa:.2f} em {tempo:.1f} anos, a prestação será de R${prestação:.2f}. Sua casa pode ser financiada!')
else:
    print('\033[31mInfelizmente sua casa não pode ser financiada.')