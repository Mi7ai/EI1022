nrList = []
while True:
    nr = int(input("Introduce un numero: "))
    if nr < 0: break
    nrList.append(nr)
nrList.sort()
for e in nrList: print(e)
