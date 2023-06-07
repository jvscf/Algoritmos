preco = float(input("Digite o preço do produto em R$: "))
cod = int(input("Digite o código de origem do produto, 1: Sul, 2: Norte, 3: Nordeste, 4: Centro-Oeste e 5: Sudeste: "))
if cod == 1:
    imp = 11
    pf = preco * (1 + imp/100)
    print(f"O produto é procedente da região Sul, com isso, sua alíquita de imposto é de {imp:.2f}% e seu preço final é de R$ {pf:.2f}.")
elif cod == 2:
    imp = 13
    pf = preco * (1 + imp / 100)
    print(f"O produto é procedente da região Norte, com isso, sua alíquita de imposto é de {imp:.2f}% e seu preço final é de R$ {pf:.2f}.")
elif cod == 3:
    imp = 9
    pf = preco * (1 + imp / 100)
    print(f"O produto é procedente da região Nordeste, com isso, sua alíquita de imposto é de {imp:.2f}% e seu preço final é de R$ {pf:.2f}.")
elif cod == 4:
    imp = 12
    pf = preco * (1 + imp / 100)
    print(f"O produto é procedente da região Centro-Oeste, com isso, sua alíquita de imposto é de {imp:.2f}% e seu preço final é de R$ {pf:.2f}.")
elif cod == 5:
    imp = 18
    pf = preco * (1 + imp / 100)
    print(f"O produto é procedente da região Sudeste, com isso, sua alíquita de imposto é de {imp:.2f}% e seu preço final é de R$ {pf:.2f}.")
else:
    print("Por favor digite o código corretamente, de 1 a 5.")