salario = float(input("Digite teu salário em R$: "))
aumento = float(input("Digite o percentual de aumento do salário: "))
nsal = salario * (1+(aumento/100))
print(f"O teu salário com um aumento de {aumento}% ficou em R$ {nsal:.2f}")