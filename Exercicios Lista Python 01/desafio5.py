temperatura_c = int(input("Digite a temperatura atual em ºC: "))

if temperatura_c < 18:
    print("Temperatura: Baixa \nSugestão: Considere ligar o aquecedor.")

elif 18 <= temperatura_c <= 25:
    print("Temperatura: Adequada \nSugestão: Não é necessário ajustar o controle climático.")

elif temperatura_c > 25:
    print("Temperatura: Alta \nSugestão: Considere ligar o ar-condicionado.") 