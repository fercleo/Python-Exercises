def leiaint(txt):
     while True:
          print('-' * 45)
          n = str(input(txt))
          if n.isnumeric():
               print(f'Você acabou de digitar o número {n}')
               break
          else:
               print('\033[31mERRO! Digite um número inteiro válido.\033[m')


#Programa principal
n = leiaint('Digite um número: ')