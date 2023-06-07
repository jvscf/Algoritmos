frase = str(input("Digite uma frase: "))
palavra = str(input("Digite uma palavra que esteja contida na frase digitada anteriormente: "))
palavras = frase.split()
cont = 0
for i in palavras:
    if i.lower() == palavra.lower():
        cont += 1
print(cont)