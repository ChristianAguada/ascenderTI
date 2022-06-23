import math

termoA = float(input('Digite o termo A da equação: '))
print("\n")
termoB = float(input('Digite o termo B da equação: '))
print('\n')
termoC = float(input('Digite o termo C da equação: '))

delta = (termoB**2)-(4*termoA*termoC)
if delta < 0:
    print('A raiz da Bhaskara é imaginária, entre com valores válidos.')
else:
    raiz = math.sqrt(delta)
    xPrimeiro = ((-termoB)+raiz)/(2*termoA)
    print(xPrimeiro)
    xSegundo = ((-termoB)-raiz)/(2*termoA)
    print(xSegundo)