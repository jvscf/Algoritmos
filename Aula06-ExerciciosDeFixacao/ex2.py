valor = float(input("Defina o valor da compra em R$: "))
if valor > 5000:
    desc = valor * 0.3
    print(f"Seu desconto é de 30%, ou seja, de R$ {desc:.2f}")
elif valor > 1000:
    desc = valor * 0.2
    print(f"Seu desconto é de 20%, ou seja, de R$ {desc:.2f}")
else:
    desc = valor * 0.1
    print(f"Seu desconto é de 10%, ou seja, de R$ {desc:.2f}")