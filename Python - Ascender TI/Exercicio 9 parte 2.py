import math

limitador = int(input('Digite um limitador para a sequencia Fibonnaci: '))
fibonacci = 1
N1 = 3
N2 = 2
cont = 0
print(fibonacci)
print(fibonacci)
print(N1)

while cont < limitador:
    fibonacci = N1 + N2
    print(fibonacci)
    N2 = N1
    N1 = fibonacci
    cont = cont + 1
    
