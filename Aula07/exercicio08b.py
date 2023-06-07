while True:
    n = int(input("Digite um número inteiro: "))
    if n >= 0:
        break
    else:
        print("Valor tem que ser maior ou igual a zero")
if (n == 0) or (n == 1):
    fat = 1
else:
    fat = 1
    for i in range(1,n+1):
        fat *= i
print(f"O valor de {n}! é igual a {fat}.")
