cont = 0
numeroDigitado = 0
menor = 1
maior = 0



while cont < 10:
    numeroDigitado = float(input('Digite um número: '))
    
       
    if numeroDigitado > maior:
        maior = numeroDigitado
    elif numeroDigitado < maior and numeroDigitado <= menor:  
        menor = numeroDigitado
    elif numeroDigitado <= menor:
        menor = numeroDigitado
    
    cont = cont + 1


print('o Maior número digitado foi: ',maior, 'o menor número digitado foi: ',menor)