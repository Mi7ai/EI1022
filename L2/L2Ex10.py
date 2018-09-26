def cuadrado(iter):
    for i in iter:
        yield i * i

g = cuadrado([1,2,10,4,5])

#los generadores no se convierten en lista, se usa un for
l = list(g)

print(l)