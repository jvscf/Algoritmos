frase = input("Digite qualquer frase: ")
vogal = 0
for letra in frase:
    if letra.lower() in "aeiouáàâãéêíóõôú":
        vogal += 1
print(f"Existem {vogal} vogais na frase")