def is_perfect(n):
    s = 0
    for i in range(1,n+1):
        if n % i == 0:
            s += i
    if s == 2*n:
        return True
    return False

# 良いと思います
