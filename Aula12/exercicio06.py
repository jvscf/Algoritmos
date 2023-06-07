def segundos(a, b, c):
    return (a * 3600 + b * 60 + c)

n = input("Digite um período de tempo com horas, minutos e segundos, separando-os com ':': ")
tempo = n.split(":")
a = int(tempo[0])
b = int(tempo[1])
c = int(tempo[2])
print(f"O período de tempo de {n} tem {segundos(a, b, c)} segundos!")