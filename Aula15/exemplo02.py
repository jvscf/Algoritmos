texto = input("Digite o texto: ")
arquivo = open("texto.txt", "w", encoding="utf-8" )
arquivo.write(texto)
arquivo.close()