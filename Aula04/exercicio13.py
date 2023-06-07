sal = float(input("Digite o valor do salário mínimo em R$: "))
kw = float(input("Digite  a quantidade de quilowatts consumida em sua residência: "))
custo = sal / 8
conta = custo * kw
desc = conta * 0.85
input(f"Cada quilowatt custa R$ {custo:.2f}, com isso, o valor a ser pago seria de R$ {conta:.2f}, R$ {desc:.2f} com 15% de desconto.")