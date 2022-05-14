num = int(input('Digite um número: '))
con = 0
for i in range(1, num +1):
    if num % i == 0:
        con += 1
print(f'O número {num} foi divisível {con} vezes.')
if con == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')