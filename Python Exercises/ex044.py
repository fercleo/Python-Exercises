preco = (float(input('Preço do produto: R$ ')))
print('FORMAS DE PAGAMENTO \n [1] à vista dinheiro/cheque \n [2] à vista no cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão')
condicao = (int(input('Condição de pagamento: ')))
avistadinch = preco/100*90
avistacartao = preco/100*95
juros = preco/100*120
if condicao == 1:
    print(f'O valor a ser pago pelo produto com 10% de desconto é: {avistadinch}.')
elif condicao == 2:
    print(f'O valor a ser pago pelo produto com 5% de desconto é: {avistacartao}.')
elif condicao == 3:
    print(f'Sua compra sera parcelada em 2x de R${preco/2}')
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas quer realizar a compra? '))
    if parcelas >= 3:
        print(f'Sua compra de {preco} irá custar o valor de {juros} com juros.')
else:
    print('Opção inválida, tente novamente.')