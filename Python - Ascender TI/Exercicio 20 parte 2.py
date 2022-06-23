numero=int(input('Digite um número para saber se ele é primo: '))

cont = 1
contPrimo = 0
while cont < 100:
    if numero % cont == 0:
        contPrimo = contPrimo + 1
    cont = cont + 1

if contPrimo == 2:
    print('O número digitado é primo, pois tem apenas: ', contPrimo, 'divisores')
else:
    print('O número digitado não é primo, pois tem: ', contPrimo, 'divisores')

