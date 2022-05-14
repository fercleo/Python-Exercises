print('===' * 10)
print('10 TERMOS DE UMA P.A')
print('===' * 10)
pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pa
c = 1
mais = 10
total = 0
while mais != 0:
   total = total + mais
   while c <= total:
      print(f'{termo}', end=' | ')
      termo = termo + r
      c += 1
   print('PAUSA')
   mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos.')