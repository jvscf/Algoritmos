idade = int(input("Digite sua idade: "))
if idade < 5:
    print("Você é muito novo(a), ainda não tem categoria.")
elif idade <= 7:
    print("Sua categoria é a Infantil.")
elif idade <= 10:
    print("Sua categoria é a Juvenil.")
elif idade <= 15:
    print("Sua categoria é a Adolescente.")
elif idade <= 30:
    print("Sua categoria é a Adulto.")
else:
    print("Sua categoria é a Sênior.")