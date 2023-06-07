def eprimo(a):
    b=0
    for i in range(1, a+1):
        if (a % i == 0):
            b += 1
    return (b == 2)

n = int(input("Digite um número: "))
if eprimo(n):
    print("O número é primo.")
else:
    print("O número não é primo.")

i = 2
j = 0
while j <= 50:
    if eprimo(i):
        print(i, end=' ')
        j += 1
    i += 1