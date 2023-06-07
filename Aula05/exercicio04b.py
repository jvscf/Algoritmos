l1 = int(input("Entre com o primeiro lado do triângulo: "))
l2 = int(input("Entre com o segundo lado do triângulo: "))
l3 = int(input("Entre com o terceiro lado do triângulo: "))
if ((l1+l2) > l3) and ((l1+l3) > l2) and ((l2+l3) > l1):
    if (l1 == l2) and (l1 == l3):
        print("triângulo equilátero")
    elif ((l1 == l2) and (l2 != l3)) or ((l1 == l3) and (l2 != l3)) or ((l3 == l2) and (l1 != l3)):
        print("triângulo isósceles")
    else:
        print("triângulo escaleno")
else:
    print("não é um triângulo")