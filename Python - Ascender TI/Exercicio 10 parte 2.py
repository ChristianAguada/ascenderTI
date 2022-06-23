hora = int(input('Digite a hora: '))
minuto = int(input('Digite os minutos: '))

anguloMinuto = (360*minuto)/60
anguloHora = 360/hora
ponteiroHora = (minuto*anguloHora)/60

anguloEntrePonteiros = anguloMinuto - ponteiroHora

print('O angulo formado entre os ponteiros do minuto e da hora é de :',anguloEntrePonteiros, 'graus')