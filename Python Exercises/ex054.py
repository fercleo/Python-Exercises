from datetime import date
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if date.today().year - nasc < 21:
        menor += 1
print(f'\n{7-menor} são Maiores e {menor} são menores.')