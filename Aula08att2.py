
def imc():
    nome = str(input("Insira o seu nome: "))
    kg = float(input("Insira seu peso em kg: "))
    h = float(input("Insira sua altura em metros: "))
    res = kg/(h**2)
    res2 = round(res, 1)
    resp = ["Abaixo do peso", "Peso normal", "Sobre Peso", "Obesidade"]
    if res2 >= 30:
        respf = resp[3]
    elif res2 < 30 and res >= 25:
        respf = resp[2]
    elif res2 < 25 and res >= 18.5:
        respf = resp[1]
    elif res2 < 18.5:
        respf = resp[0]
    else:
        respf = "Algo não bate"
    return(res2 ,respf)
print(imc())