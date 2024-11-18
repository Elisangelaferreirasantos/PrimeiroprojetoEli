lista =['banana', 'maça' , 'pera' ,'banana']
tupla = (1, 2, 3, 4, 5)
meu_set = (1, 2, 3, 4)
dicionario = {"nome": "Caique", "idade": 22}



def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("Limão" , "Morango")

for frutas in lista:
    print (f"os elementos contidos na lista são: {frutas}")
    