n = int(input("Digite um número inteiro maior que 1: "))
b = 0
for i in range(1, n+1):
    if (n % i == 0):
        b += 1
if b == 2:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")
