from funcoes import dado
from time import sleep
while True:
    entrada = input("Bem vindos ao jogo 'Tem dado em casa?', Digite <Enter> para rolar seu dado.")
    user = dado()
    print(f"Você tirou {user}!")
    for j in range(0,3):
        for i in range(0,3):
            print(".", end='')
            sleep(0.5)
        print("        ", end='\r')
    pc = dado()
    print(f"Tirei {pc}!")
    if user > pc:
        print(f"Você ganhou! {user} é maior que {pc}...")
    elif user == pc:
        print(f"Eita, empatamos! {user} é igual a {pc}...")
    else:
        print(f"Ganhei! {pc} é maior que {user}...")
    denovo = input("Quer jogar novamente? (S/N): ")
    if denovo.upper() == "N":
        break





