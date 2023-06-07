degrau = float(input("Digite a altura de cada degrau em cm: "))
altura = float(input("Digite a altura que deseja subir com a escada em m: "))
degraus = (altura * 100) / degrau
print(f"A escada vai ter {degraus:.0f} degraus.")