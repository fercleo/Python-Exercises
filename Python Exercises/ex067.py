c = 0
while True:
    t = int(input('Digite um número inteiro que te daremos a sua tabuada: (número negativo para encerrar o programa) '))
    print('-'*15)
    if t < 0:
        break
    while c < 10:
        c += 1
        print(f'{t} * {c} = {t*c}')
    print('-'*15)
    c = 0 #para zerar o contador e poder iniciar uma nova tabuada do 1 ao 10
print('Programa da tabuada encerrado.')