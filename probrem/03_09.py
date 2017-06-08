def my_filter(range_obj,f):
    for i in range_obj:
        if f(i):
            print(i)
