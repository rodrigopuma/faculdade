valor_original = float(input("Digite o valor total da compra: R$\n").replace(',','.'))

desconto = 10 / 100

if valor_original >= 200.0:
    valor_desconto = valor_original * (1 - desconto)
else:
    valor_desconto = valor_original

print(f"Valor original: R${f'{valor_original:.2f}'.replace('.',',')}")

if valor_desconto == valor_original:
    print("Nenhum desconto aplicado")

elif valor_desconto < valor_original:
    print(
f"""Desconto aplicado: R${f'{valor_original * desconto:.2f}'.replace('.',',')}
Valor final: R${f'{valor_desconto:.2f}'.replace('.',',')}"""
    )
