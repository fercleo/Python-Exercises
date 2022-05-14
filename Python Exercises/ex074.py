from random import sample
a = tuple(sample(range(100),5))
print(f'Os números gerados foram {a}')
print(f'O maior valor é {max(a)} e o menor valor é {min(a)}.')