def filter(f,iter):
    for i in iter:
        if f(i):
            yield i

#print(list(filter(lambda n: n%2 == 0, [2,4,5,7,2])))