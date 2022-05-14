from random import randint
from time import sleep
print('*x*' * 15)
print('PEDRA PAPEL E TESOURA')
print('*x*' * 15)
print('Suas opções: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA')
jogador = int(input('Escolha: '))
pc = randint(0, 2)
print('JO \n KEN \n PÔ!!!')
sleep(2)
print('*x*' * 15)
print(f'Computador jogou {pc} e o jogador jogou {jogador}.')
print('*x*' * 15)
if jogador == 0 and pc == 2:
    print('Parabéns! Você venceu!')
elif jogador == 2 and pc == 0:
    print('O computador venceu!')
elif jogador == 0 and pc == 1:
    print('O computador venceu!')
elif jogador == 1 and pc == 0:
    print('Parabéns! Você venceu!')
elif jogador == 2 and pc == 1:
    print('Parabéns! Você venceu!')
elif jogador == 1 and pc == 2:
    print('O computador venceu!')
elif jogador == pc:
    print('Empate!')

