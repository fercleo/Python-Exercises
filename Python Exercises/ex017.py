from math import hypot
oposto = float(input('\033[37mQual o comprimento do cateto oposto? '))
adjacente = float(input('\033[37mQual o comprimento do cateto adjacente? '))
soma = hypot(oposto, adjacente)
print(f' \033[37mA hipotenusa irá medir {soma:.2f}')
