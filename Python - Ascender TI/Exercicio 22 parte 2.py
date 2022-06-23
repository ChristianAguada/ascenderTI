numeroA = int(input('Digite um número:'))
numeroB = int(input('Digite outro número:'))
cont = 0
resultado = 0

while cont < numeroB:
    resultado = resultado + numeroA
    cont = cont + 1


print('O resultado do produto entre,', numeroA,'e o número,',numeroB,' é de :', resultado)
