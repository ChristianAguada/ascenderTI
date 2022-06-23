num = float(input('Digite um número: '))
fat = num
contador = num-1
while contador > 0:
    fat = fat*contador
    contador = contador-1

print('O número digitado foi: ',num, 'e o seu fatorial é: ',fat)