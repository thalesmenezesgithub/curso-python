compra = input("Digite o valor da compra: ")
valorCompra = float(compra)

frete = input("Digite o valor do frete: ")
valorFrete = float(frete)

fidelidade = input("Cliente é cadastrado no programa fidelidade? “s” (sim) ou “n” (não) ")
fidelidade = str(fidelidade)


total = valorCompra + valorFrete

if (total >= 100) or (fidelidade == "s"):
    print("Cupom de desconto aplicado com sucesso!")
    
else:
    print("Não foi possível aplicar o cupom de desconto!")