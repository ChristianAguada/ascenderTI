numMacas = float(input('Informe um número de maçãs que deseja comprar: '))
precoMacas = 0.50
if numMacas <= 10:
    custoTotal = precoMacas * numMacas
    print('O custo total da sua compra é de: R$', custoTotal)
elif numMacas >10 and numMacas <= 20:
     precoMacas = 0.40
     custoTotal = precoMacas * numMacas
     print('O custo total da sua compra é de: R$', custoTotal)
elif numMacas > 20:
     precoMacas = 0.30
     custoTotal = precoMacas * numMacas
     print('O custo total da sua compra é de: R$', custoTotal)
