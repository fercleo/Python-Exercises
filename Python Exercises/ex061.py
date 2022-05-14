print('===' * 10)
print('10 TERMOS DE UMA P.A')
print('===' * 10)
pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pa
c = 1
while c <= 10:
   print(f'{termo}', end=' | ')
   termo = termo + r
   c += 1
print('Fim')