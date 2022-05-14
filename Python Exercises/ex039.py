from datetime import date
ano = (int(input('Ano de nascimento: ')))
nascimento = date.today().year-ano
ano_alistamento = ano+18
anoatual = date.today().year
if nascimento < 18:
    print(f'Falta(m) {18-nascimento} ano(s) pro seu alistamento. \nVocê tem {nascimento} ano(s) em {anoatual}. \nSeu alistamento será em {ano_alistamento}.')
elif nascimento == 18:
    print('Você está na idade de se alistar.')
else:
    print(f'Já se passaram {nascimento-18} anos da sua data de alistamento.')
