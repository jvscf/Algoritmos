from random import randint
dado1 = [0]*7
dado2 = [0]*7
dados = [0]*13
for i in range(30000):
    x = randint(1, 6)
    y = randint(1, 6)
    soma = x + y
    dado1[x] += 1
    dado2[y] += 1
    dados[soma] += 1
print(dados)
stat = [0]*13
for i in range(2, 13):
    stat[i] = dados[i] / 30000
    print(f"A soma {i} foi sorteada {dados[i]} vezes, ou seja, {stat[i]:.2%} das vezes.")