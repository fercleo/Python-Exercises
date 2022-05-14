listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Você digitou os valores {listanum}.')
print(f'O maior número foi {max(listanum)} nas posições ', end= '')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}... ', end ='')
print()
print(f'O menor número foi {min(listanum)} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}...', end='')
