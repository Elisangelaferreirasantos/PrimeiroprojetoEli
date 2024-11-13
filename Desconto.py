# Detalhes da compra
nome = "ELI SANTOS"
mes_compra = "JANEIRO"
valor_compra = 550.00
desconto = 10 # percentual de desconto

# Calcular o valor do desconto
valor_desconto = valor_compra * (desconto / 100)
valor_com_desconto = valor_compra - valor_desconto

# Detalhes do cupom
cupom = "ELIÉ10"

# Exibir resultado
print(f"Olá {nome}. Em {mes_compra} você fez uma compra no valor de R${valor_compra:.2f} e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom}.")
print(f"Valor com desconto: R${valor_com_desconto:.2f}")

