from L2.L2Ex11 import first,take_while
def squares():
    n=1
    while True:
        yield n*n
        n +=1

def escapicua(n):
    a = str(n)
    b = a[::-1]
    return a==b

a = first(100,squares())
b = take_while(lambda n: ,squares())
c = first(10, filter(escapicua,squares()))

print(list(c))
