peso = float(input('Informe o seu peso para o calculo do IMC: '))
altura = float(input('Informe a sua altura EM METROS para o calculo do IMC: '))

imc = peso / (altura**2)

print('O seu IMC é de: ', imc)
if imc > 25 and imc < 35:
    print('TRUE')
