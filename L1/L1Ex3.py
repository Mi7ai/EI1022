d = {'M1':20,'M2':21,'M3':22}

name = input("Dime tu nombre: ")
if name in d:
    print(d[name])
else:
    print("Nombre no existe...")