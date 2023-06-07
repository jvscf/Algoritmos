somapeso = 0
somaaltura = 0
imc=[]
i = 1
while i <= 20:
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em m: "))
    somapeso += peso
    somaaltura += altura
    imc.append(peso/altura**2)
    i += 1
pesomedio = somapeso / 20
alturamedia = somaaltura / 20
maiorimc = max(imc)
menorimc = min(imc)
print(f"O peso médio é {pesomedio:.2f}kg, a altura média é {alturamedia:.2f}m, o maior IMC foi {maiorimc:.2f} e o menor IMC foi {menorimc:.2f}.")