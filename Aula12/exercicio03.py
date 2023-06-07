def bissexto(a):
    if (a % 4 == 0):
        if (a % 100 == 0):
            if (a % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

n = int(input("Digite o ano: "))
if bissexto(n):
    print("Ano bissexto!")
else:
    print("Ano não bissexto!")
