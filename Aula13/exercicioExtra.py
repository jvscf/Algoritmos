def triangular(n):
    for i in range(3,n+1):
        if (i*(i-1)*(i-2)) == n:
            return True
    return False
print(triangular(120))
