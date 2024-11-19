matricula = int(input("Insira seu número de matrícula: "))

def par_ou_impar(matricula):
    if matricula % 2 == 0:
        return ("VOCÊ ESTÁ NO TIME AZUL")
    
    else : return ("VOCÊ ESTÁ NO TIME AMARELO")

print(par_ou_impar(matricula))