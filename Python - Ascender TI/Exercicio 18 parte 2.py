cont = 0
contNegativo = 0
contPositivo = 0


while cont < 10:
    numeroDigitado = int(input('Digite um número: '))
    if numeroDigitado < 0:
        contNegativo = contNegativo + 1
    else:
        contPositivo = contPositivo + 1
    cont = cont + 1

print('Dos números digitados,', contNegativo,' são negativos e ',contPositivo, 'são positivos.')