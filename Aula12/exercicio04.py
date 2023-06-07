from math import gcd

def mdc(a, b):
    return (abs(a * b) / gcd(a, b))

print(int(mdc(5, 4)))