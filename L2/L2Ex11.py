def first(n,iter):
    for i in iter:
        if n == 0: break
        yield i
        n -=1

#print(list(first(20, range(50, 200))))