sexo = str(input("Digite seu sexo, M para masculino e F para feminino: "))
h = float(input("Entre com sua altura em m: "))
if sexo.upper() == "M":
    p = (72.7 * h) - 58
    print(f"Seu peso ideal é {p:.1f}kg")
else:
    if sexo.upper() == "F":
        p = (62.1 * h) - 44.7
        print(f"Seu peso ideal é {p:.1f}kg")
    else:
        print("Não aceitamos não binare, ou é M ou é F!!")
