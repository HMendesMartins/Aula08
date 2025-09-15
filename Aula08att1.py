
def economia():
    nome = str(input("Insira o seu nome: "))
    km = int(input("Insira a a quantidade de km percorridos: "))
    litros = int(input("Insira quantos litros de gasolina foram gastos na viagem: "))
    res = km/litros
    resp = ["Econômico", "Regular", "Alto consumo"]
    if res >= 15:
        respf = resp[0]
    elif res < 15 and res >= 10:
        respf = resp[1]
    elif res < 10 and res >=0:
        respf = resp[2]
    else:
        respf = "Algo não bate"
    return(respf)
print(economia())