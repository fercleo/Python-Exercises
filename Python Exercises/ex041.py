from datetime import date
nascimento = (int(input('Ano de nascimento: ')))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print(f'O atleta tem {idade} anos. Sua classificação é \033[32mmirim.\033[m')
elif idade <= 14:
    print(f' O atleta tem {idade} anos. Sua classificação é \033[31minfantil.\033[m')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. Sua classificação é \033[33mjúnior.\033[m')
elif idade <= 25:
    print(f'O atleta tem {idade} anos. Sua classificação é \033[34msênior.\033[m')
elif idade > 25:
    print(f'O atleta tem {idade} anos. Sua classificação é \033[35mmaster.\033[m')