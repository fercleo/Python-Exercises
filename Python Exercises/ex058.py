from random import randint

print('.=-' * 23)
print('Vou pensar num número entre 0 e 10. Tente adivinhar qual é o número.')
print('.=-' * 23)
numero = int(input('Tente adivinhar: '))
aleat = randint(0,10)
tent = 1
while numero != aleat:
    numero = int(input('Errou. Tente outra vez: '))
    tent = tent+1
    if aleat > numero:
        print('Mais.')
    elif aleat < numero:
        print('Menos.')
print(f'Parabéns, você venceu! Foram necessárias {tent} tentativas.')