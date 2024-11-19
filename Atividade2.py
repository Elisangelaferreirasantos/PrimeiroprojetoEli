def verificar_grupo(matricula):
    if matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

matricula_input = input("Digite seu número de matrícula: ")

if matricula_input.isdigit():  
    matricula = int(matricula_input)
    verificar_grupo(matricula)
else:
    print("Número inválido. Por favor, digite um número inteiro válido.")
