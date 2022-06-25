print('Bem vindo(a) a Loja da Thamires!!!')
print('')
valor = float(input('Entre com o valor do produto:'))
quant = int(input('Entre com a quantidade do produto:'))

subtotal = valor * quant

if quant >=10 and quant <=99:
    total = subtotal - (subtotal * 5/ 100)
    print('Valor sem desconto:R${:.2f}'.format(subtotal))
    print('Valor com desconto:R${:.2f} - Desconto de 5%'.format(total))

elif quant >=100 and quant <=999:
    print('O valor do desconto foi:')
    total = subtotal - (subtotal * 10 / 100)
    print('Valor sem desconto:R${:.2f}'.format(subtotal))
    print('Valor com desconto:R${:.2f} - Desconto de 10%'.format(total))

elif quant >=1000:
    print('O valor do desconto foi2:')
    total = subtotal - (subtotal * 15 / 100)
    print('Valor sem desconto:R${:.2f}'.format(subtotal))
    print('Valor com desconto:R${:.2f}- Desconto de 15%'.format(total))

else:
    print('Valor sem desconto:R${:.2f}'.format(subtotal))
    print('Não houve desconto!')
