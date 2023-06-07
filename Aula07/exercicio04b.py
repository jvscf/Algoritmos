n = ""
i = 0
soma = 0
while n != 0:
    n = int(input("Digite sua idade ou 0 para cancelar: "))
    soma += n
    i += 1
media = soma / (i - 1)
print(media)
print(i-1)