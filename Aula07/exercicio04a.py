somapar = 0
n = ""
i = 0
while n != 0:
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        somapar += n
        i += 1
mediapar = somapar / i
print(mediapar)