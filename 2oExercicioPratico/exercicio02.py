def eprimo(a):
    b=0
    for i in range(1, a+1):
        if (a % i == 0):
            b += 1
    return (b == 2)

def qtsprimos(a):
    lista = []
    for i in range(0,a):
        if eprimo(i):
            lista.append(i)
    return lista

print(qtsprimos(25))

soma=0
for i in range(0, len(qtsprimos(25))):
    soma += qtsprimos(25)[i]
print(soma)
