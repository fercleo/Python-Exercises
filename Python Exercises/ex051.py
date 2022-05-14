print('===' * 10)
print('10 TERMOS DE UMA P.A')
print('===' * 10)
pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(f'{pa + r * c}', end=' | ')
print('--Fim--')