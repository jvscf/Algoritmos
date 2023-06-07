dic = {}

for i in range(10):
    x = input(f"Digite o sobrenome da {(i + 1)}a. pessoa: ")
    y = input(f"Digite a idade da {(i + 1)}a. pessoa: ")
    dic[x] = y

print(dic)
print(max(dic, key=dic.get))