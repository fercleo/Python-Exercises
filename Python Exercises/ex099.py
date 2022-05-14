def maior(*num):
    if len(num) > 0:
        print(f'O maior número é {max(num)}')
    else:
        print(f'Inválido.')

maior(2, 4, 5, 9)
maior()
maior(5, 12, 25, 98)
