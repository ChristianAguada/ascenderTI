anguloA = float(input('Digite o Angulo A do triangulo: '))
print("\n")
anguloB = float(input('Digite o Angulo B do triangulo: '))
print('\n')
anguloC = float(input('Digite o Angulo C do triangulo: '))

if (anguloA < 90 and anguloB < 90 and anguloC < 90):
    print('O triangulo é Acutângulo!')
elif (anguloA == 90 or anguloB == 90 or anguloC == 90):
    print('O triangulo é Retângulo!')
elif (anguloA > 90 or anguloB > 90 or anguloC > 90):
    print('O triangulé Obtusângulo')