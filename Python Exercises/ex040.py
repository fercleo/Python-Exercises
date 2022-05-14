primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira+segunda) / 2
if media >= 7.0:
    print('\033[32mParabéns, você está aprovado!')
elif media < 4.0:
    print('\033[31mQue pena... Você reprovou :(')
elif media >= 4.0 < 7.0:
    print('\033[33mVocê está de recuperação. Capriche nos estudos para passar no exame final.')