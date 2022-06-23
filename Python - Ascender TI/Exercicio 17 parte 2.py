cont = 0
contPares = 0
contImpares = 0


while cont < 10:
    numeroDigitado = int(input('Digite um número: '))
    if numeroDigitado % 2 == 0:
        contPares = contPares + 1
    else:
        contImpares = contImpares + 1
    cont = cont + 1

print('Dos números digitados,', contPares,' são pares e ',contImpares, 'são ímpares.')