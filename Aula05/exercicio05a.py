import datetime
nasc = int(input("Digite teu ano de nascimento: "))
hj = datetime.date.today()
ano = hj.year
idade = ano - nasc
if idade >= 16:
    if idade >= 18:
        print(f"Você tem {idade} anos, com isso, já pode votar e tirar a CNH.")
    else:
        print(f"Você tem {idade} anos, com isso, já pode votar, porém ainda não pode tirar a CNH.")
else:
    print(f"Você tem {idade} anos, com isso, ainda não pode votar nem tirar a CNH.")
