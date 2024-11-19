tupla = (1, 2, 3, 4, 5)

lista = list(tupla)

lista.append(6)
lista.append(7)

lista.pop(0)
lista.pop(-1)
print("Primeiro dado da lista:", lista[0])
print("Quantidade de dados na lista:", len(lista))

dicionario = {"Nome": "Eli", "Idade": 45, "Profissão": "TI"}
print("Nome do dicionário:", dicionario["Nome"])
