m = int(input("Digite um número inteiro e positivo: "))
n = int(input("Digite um número inteiro e positivo que seja menor que o anterior: "))
if n >= m:
    print("O último número digitado deve ser menor que o primeiro!")
else:
    soma = 0
    i = n
    while i <= m:
        soma += i
        i += 1
print(soma)