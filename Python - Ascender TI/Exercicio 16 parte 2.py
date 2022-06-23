cont = 0
somatorio = 0
media = 0



while cont < 10:
    numeroDigitado = float(input('Digite um número: '))
    somatorio = numeroDigitado + somatorio
    cont = cont + 1



media = somatorio / cont

print('A média dos números digitados é: ',media)