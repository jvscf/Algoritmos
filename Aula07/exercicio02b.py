while True:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    if base and altura > 0:
        break
    else:
        print("O valor deve ser positivo e diferente de zero")
area = (base * altura) / 2
print(f"A área do triângulo é de {area:.2f} m2")