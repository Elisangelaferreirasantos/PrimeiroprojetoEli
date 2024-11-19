lista =['banana', 'maça' , 'pera' ,'banana']
tupla = (1, 2, 3, 4, 5)
meu_set = (1, 2, 3, 4)
dicionario = {"nome": "Caique", "idade": 22}



def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("Limão" , "Morango")

var_txt = "texto"
for letras in var_txt:
        print (letras)

for x in lista:
    print (f"Os elementos contidos na lista são: {x}")

    dicionario = {"nome": "Caique" , "idade": 22}
    for chave in dicionario:
         print(f"As chaves neste dicionario são: {chave}")

         for w in dicionario.values():
              print (f"Os valores neste dicionario são: {w}")
            

dicionario = {"nome": "Caique" , "idade": 22}

for chave,valor in dicionario.items():
     print(dicionario["idade"])
     print(dicionario["nome"])
     print(f"chave: {chave}, valor: {"valor"}")

    
          
lista1 = ['Banana', 'Maçã', 'Uva']

def add_frutas(a,b):
     lista1.append(a)
     lista1.append(b)
     print(lista1)

add_frutas("Abacte" ,"Sorvete")

def del_frutas():
         lista1.pop()
         print(lista1) 

del_frutas()

for x in lista1:
      print(f"Esta fruta esta na lista {x}")







