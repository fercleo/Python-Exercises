from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogadorX': randint(1, 6),
         'jogadorW': randint(1, 6),
         'jogadorY': randint(1, 6),
         'jogadorZ': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(' ** RANKING DOS JOGADORES **')
for i, v in enumerate(ranking):
    print(f' O {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)