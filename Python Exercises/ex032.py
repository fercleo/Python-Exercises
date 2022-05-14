from datetime import date
ano = int(input('Digite um ano para saber se ele é ou não bissexto. Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[33;40mO ano {ano} é bissexto.\033[m')
else:
    print(f'\033[33;40mO ano {ano} não é bissexto.\033[m')
