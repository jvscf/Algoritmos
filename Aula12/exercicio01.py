def parouimpar(a):
    return (a % 2 == 0)

n = int(input("Digite um número: "))
if parouimpar(n) == True:
    print("O número é par.")
else:
    print("O número é ímpar.")