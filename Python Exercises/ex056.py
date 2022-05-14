sidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
menosvinte = 0
for p in range(1, 5):
    nome = input(f'Digite o nome da {p} pessoa: ').strip()
    idade = int(input(f'Digite a idade da {p} pessoa: '))
    sexo = input(f'Digite o sexo da {p} pessoa (M/F): ').strip()
    sidade += idade
    if sexo in 'Ff' and idade < 20:
        menosvinte += 1
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
mediaidade = sidade/4
print(f'A média de idade do grupo é {mediaidade} ')
print(f'O homem mais velho tem {maioridadeh} anos e se chama {nomevelho}.')
print(f'{menosvinte} mulher(es) tem menos de 20 anos.')
