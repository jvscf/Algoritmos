nasc = int(input("Qual ano você nasceu? "))
atual = int(input("Em que anos estamos? "))
anos = atual - nasc
meses = anos * 12
dias = anos * 365
semanas = anos * 52
print(f"Você tem {anos} anos, {meses} meses, {semanas} semanas e {dias} dias.")