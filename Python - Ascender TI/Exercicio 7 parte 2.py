from cmath import pi
import math

raioCircunferencia = float(input('Digite o raio da circunferência: '))
print("\n")
areaCirculo = (3.14*raioCircunferencia**2)
perimetroCirculo = (2*3.14*raioCircunferencia)

if areaCirculo > 10:
    print('A área do circulo é superior a 10: ', areaCirculo)

if perimetroCirculo > 10:
    print('O perímetro do circulo é superior a 10: ', perimetroCirculo)