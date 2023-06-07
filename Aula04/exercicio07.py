deposito = float(input("Digite o valor do depósito em R$: "))
juros = float(input("Digite a taxa de juros em %: "))
rendimento = deposito * (juros/100)
vf = deposito + rendimento
print(f"O seu depósito de R$ {deposito:.2f} rendeu {juros}%, um rendimento total de R$ {rendimento:.2f}, o deixando com R$ {vf:.2f}.")