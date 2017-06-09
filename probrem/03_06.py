def my_sum(*arg):
    s = 0
    for x in arg:
        s += x
    return s

if __name__ == '__main__':
    print(my_sum(1,2,3))
    print(my_sum(1,2,3,4,5))
# いいですね
