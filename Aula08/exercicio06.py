palavra = str(input("Digite uma palavra: "))
arvalap = palavra.lower()[::-1]
if palavra.lower() == arvalap:
    print(f"A palavra {palavra} é um palíndromo.")
else:
    print(f"A palavra {palavra} não é um palíndromo.")
