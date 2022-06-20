idade = int(input('Digite a sua idade para verificar a obrigatoriedade do voto: '))
if idade >= 18 and idade <=60:
    print('Como você informou que tem', idade, 'anos de idade o voto é obrigatório.')
else:
    print('Como você informou que tem', idade, 'anos de idade o voto não é obrigatório.')