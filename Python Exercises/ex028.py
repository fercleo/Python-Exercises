from random import randint
from time import sleep

print('.=-' * 23)
print('Vou pensar num número entre 0 e 5. Tente adivinhar qual é o número.')
print('.=-' * 23)
numero = int(input('Em qual número eu pensei? ')) #O jogador tenta adivinhar
numero1 = randint(0, 5) #Faz o PC Pensar
print('Processando...')
sleep(2)
if numero == numero1:
    print('Parabéns, você acertou!') #Se o jogador acertar
else:
    print(f'Você errou. Eu pensei no número {numero1} e não no {numero}.') #Se o jogador errar
print('--FIM--')

