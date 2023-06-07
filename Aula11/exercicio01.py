t = ()
for i in range(10):
    x = int(input(f"Digite o {i+1}o. número: "))
    t += (x,)

print(t[::-1])