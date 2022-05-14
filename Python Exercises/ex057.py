sexo = str(input('Qual seu sexo? [m/f]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Digite novamente: ')).upper()[0].strip()
print(f'Ok. Seu sexo foi registrado como {sexo}.')


