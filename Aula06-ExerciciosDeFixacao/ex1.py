x = int(input("Defina um número inteiro: "))
if (x % 5 == 0) and (x % 3 == 0):
    print(f"{x} é divisível por 5 e por 3 ao mesmo tempo")
else:
    print(f"{x} não é divisível por 5 e por 3 ao mesmo tempo")