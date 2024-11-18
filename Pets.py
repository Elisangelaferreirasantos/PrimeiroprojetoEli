# Entradas do usuário
nome_pet = input("Qual o nome do seu pet? ")
idade_humana = int(input("Qual a idade do seu pet em anos humanos? "))
porte = input("Qual o porte do seu pet? (grande, medio, pequeno): ").lower()
numero_banhos = int(input("Quantos banhos o seu pet tomou nos últimos 12 meses? "))

# Calculando a idade do pet em anos de pet
idade_pet = idade_humana * 7

# Definindo preço e custo do banho com base no porte
if porte == "grande":
    preco_banho, custo_banho = 75, 20
elif porte == "medio":
    preco_banho, custo_banho = 60, 15
elif porte == "pequeno":
    preco_banho, custo_banho = 50, 5


# Calculando o lucro
lucro = (preco_banho - custo_banho) * numero_banhos

# Exibindo o resultado
print(f"Olá, {nome_pet} tem {idade_pet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")
