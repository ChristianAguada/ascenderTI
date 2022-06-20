qtdReais = float(input('Digite a quantidade de reais a ser convertida em pesos: '))
qtdPeso = qtdReais * (1.6)

print(qtdReais ,'reais informados equivalem a:', qtdPeso, 'pesos.')

if qtdPeso > 100:
    print('True - O valor excede 100 pesos')
