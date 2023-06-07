p1 = float(input("Digite a primeira nota (0 a 10): "))
p2 = float(input("Digite a segunda nota (0 a 10): "))
p3 = float(input("Digite a terceira nota (0 a 10): "))
media = (p1 + p2 + p3) / 3
if media >= 7:
    print(f"Sua média foi de {media:.1f}, parabéns, você foi aprovado!")
else:
    if media >= 3:
        exame = 12 - media
        print(f"Sua média foi de {media:.1f}, você está de exame e precisa de {exame:.1f} para passar")
    else:
        print(f"Sua média foi de {media:.1f}, você foi reprovado.")