with open("frutas.txt", "a", encoding="utf-8") as arquivo:
    while True:
        fruta = input("Digite uma fruta: ")
        if fruta == "":
            break
        else:
            arquivo.write(f"{fruta}\n")
