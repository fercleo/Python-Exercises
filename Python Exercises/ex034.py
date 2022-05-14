salario = float(input('Qual o salário do funcionário? '))
if salario > 1250:
    salarionovo = salario*1.10
else:
    salarionovo = salario*1.15
print(f'O funcionário que tinha um salário de {salario:.2f} passa a ter agora um salário de {salarionovo:.2f}')