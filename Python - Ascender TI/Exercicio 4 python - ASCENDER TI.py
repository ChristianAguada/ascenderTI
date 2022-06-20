valProduto = float(input('Digite o valor do produto adquirido: '))
pagRecebido = float(input('Digite o montante pago em dinheiro: '))
trocoCliente = pagRecebido - valProduto

print('O troco a ser entregue ao cliente é de: R$', trocoCliente)