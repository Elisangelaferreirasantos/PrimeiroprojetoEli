# Função para calcular a idade do pet em anos de cachorro
def calcular_idade_pet(idade_humana):
    return idade_humana * 7

# Função para calcular o lucro anual com banhos
# calcular_lucro_anual(tipo, banhos_por_ano):
    if tipo == "grande":
        preco_banho = 75.00
        custo_banho = 20.00
    elif tipo == "medio":
        preco_banho = 60.00
        custo_banho = 15.00
    elif tipo == "pequeno":
        preco_banho = 50.00
        custo_banho = 5.00
    else:
        raise ValueError("Tipo de cachorro inválido")

    lucro_por_banho = preco_banho - custo_banho
    lucro_anual = lucro_por_banho * banhos_por_ano
    return lucro_anual

# Exemplo de uso
nome = "Tuco"
idade_humana = 5
tipo = "grande"
banhos_por_ano = 10

idade_pet = calcular_idade_pet(idade_humana)
lucro_anual = (calcular_lucro_anual(tipo, banhos_por_ano))

print(f"Olá, {nome} tem {idade_pet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_anual:.2f}")
