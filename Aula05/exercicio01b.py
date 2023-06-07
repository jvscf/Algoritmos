n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
media = (n1 + n2) / 2
if n1 > n2:
    dif = n1 - n2
elif n1 == n2:
    dif = 0
else:
    dif = n2 - n1
prod = n1 * n2
div = n1 / n2
print(f"A média entre os dois números é {media:.2f}, a diferença do maior pelo menor é de {dif:.2f}, o produto entre os dois é {prod:.2f} e a divisão do primeiro pelo segundo é {div:.2f}.")
