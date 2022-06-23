valProduto = float(input('Digite o valor do produto: R$'))
valRecebido = float(input('Digite a quantia recebida em dinheiro: R$'))

troco = valRecebido - valProduto

if valRecebido < valProduto:
    print('O cliente ainda deve: R$', valProduto-valRecebido)
elif valRecebido == valProduto:
    print('O cliente não tem direito a troco')
elif valRecebido > valProduto:
    print('O valor do troco a ser dado ao cliente é de: R$', troco)
