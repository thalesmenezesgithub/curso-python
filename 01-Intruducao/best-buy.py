valor_compras = 389.98 #valor total da compra
quant_itens = 2
desconto = valor_compras * 0.1

#realiza o calculo total final com desconto
final_compras = valor_compras - desconto

custo_medio = final_compras / quant_itens

print("Valor final das compras com desconto: R$", final_compras)
print("Custo médio de cada ítem: R$", custo_medio)
