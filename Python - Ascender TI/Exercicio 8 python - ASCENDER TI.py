
distancia = float(input('Informe a distância a ser percorrida em KM: '))
custoCombustivel = float(input('Informe o custo atual do litro do combustível R$: '))
mediaVeiculo = float(input('Informe a média de consumo do veículo, conforme o fabricante: '))

print('A distancia a ser percorrida informada foi de: ', distancia)
print('O custo do litro do combustivel informado foi de R$: ', custoCombustivel, '/litro')
print('A média de consumo do veículo informado foi de: ', mediaVeiculo, 'km/litro')

gastoCombustivel = distancia / mediaVeiculo * custoCombustivel

print('Com base nos dados informados, o custo total com combustível em sua viagem é de: R$', gastoCombustivel)