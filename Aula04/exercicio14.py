hora = float(input("Digite um horário no formato hh.mm: "))
mins = int(hora) * 60 + (hora - int(hora)) * 100
print(f"O horário {hora:2.2f} tem {mins:.0f} minutos.")