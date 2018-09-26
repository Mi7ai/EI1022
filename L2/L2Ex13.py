def take_while(f,iter):
    for i in iter:
        if not f(i): break
        yield i