larg = float(input("Defina a largura do aposento em m: "))
compr = float(input("Defina o comprimento do aposento em m: "))
tinta = float(input("Escolha o volume da lata de tinta, 1L, 3.6L ou 18L: "))
a = 1
b = 3.6
c = 18
if tinta >= 18:
    tinta == c
elif tinta >= 3.6:
    tinta == b
else:
    tinta == a
area = 2 * (2.8 * larg) + 2 * (2.8 * compr) - 2.1 * 0.8
litros = area / 3
latas = litros / tinta
latasint = int(latas)
if (latas - latasint) < 0:
    latotal = latasint
else:
    latotal = latasint + 1
print(f"Você vai precisar de {latotal} latas de tinta de {tinta}L para pintar {area:.2f} m2 de parede.")
