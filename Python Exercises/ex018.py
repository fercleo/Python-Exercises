import math
angulo = float(input('Qual o ângulo? '))
radians = math.radians(angulo)
seno = math.sin(radians)
cos = math.cos(radians)
tan = math.tan(radians)
print(f' O ângulo de {angulo} terá o seno de {seno:.2f}, o cosseno de {cos:.2f} e a tangente de {tan:.2f}.')
