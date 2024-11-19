def verificar_grupo(matricula):
    if matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

try:
    matricula = int(input("Digite seu número de matrícula: "))
    verificar_grupo(matricula)
except ValueError:
    print("Número inválido. Por favor, digite um número inteiro válido.")
