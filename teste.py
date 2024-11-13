nome = input("Digite seu nome: ")
mes = input("Digite o mês da compra: ")
valor_compra = float(input("Digite o valor da compra: R$ "))
desconto = 10
cupom_de_desconto = (nome + "É10")

print(f"Olá, {nome} Em {mes} você fez uma compra no valor de R$ {valor_compra} e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom_de_desconto}")

