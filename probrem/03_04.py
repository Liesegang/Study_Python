def is_prime(n):
    if n == 2:
        return True
    else:
#       range(2, n**0.5 + 1) とかするとちょっと早くなります
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    for x in range(4,102,2):
        for y in range(2,x):
            if (is_prime(y)) and (is_prime(x-y)):
#               デフォルトで，半角スペースがsepに指定されているのでわざわざ指定しなくて大丈夫です
                print(str(x),str(y),str(x-y),sep=' ')
                break

# 良いですね！
