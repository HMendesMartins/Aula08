
def veloc():
    nome = str(input("Insira o seu nome: "))
    kg = int(input("Insira a velocidade registrada(km/h): "))
    resp = ["Dentro do limite", "Acima do limite(leve)", "Acima do limite(grave)"]
    if kg <= 80:
        respf = resp[0]
    elif kg > 80 and kg < 100:
        respf = resp[1]
    elif kg >= 100:
        respf = resp[2]
    else:
        respf = "Algo não bate"
    return(respf)
print(veloc())