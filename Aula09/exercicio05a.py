from random import randint
dado = [0]*7
for i in range(6000):
    x = randint(1, 6)
    dado[x] += 1
print(dado)
stat = [0]*7
for i in range(1, 7):
    stat[i] = dado[i] / 6000
    print(f"O lado {i} foi sorteado {dado[i]} vezes, ou seja, {stat[i]:.2%} das vezes.")