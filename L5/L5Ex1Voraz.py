from typing import *


def mientras_quepa(W: List[int], C: int) -> List[int]:  # Utilizamos append
    espacio_contenedor = C
    ultimo_contenedor = 0
    mq = []
    for v in range (len(W)):
        if(W[v] <= espacio_contenedor):
            mq.append(ultimo_contenedor)
            espacio_contenedor -= W[v]
        else:
            ultimo_contenedor += 1
            mq.append(ultimo_contenedor)
            espacio_contenedor = C -W[v] #

    return mq


def mientras_quepa_V2(W: List[int], C: int) -> List[int]: # Sin utilizar append
    espacio_contenedor = C
    ultimo_contenedor = 0
    mq = [-1] * len(W)
    for i in range (len(W)):
        if(W[i] <= espacio_contenedor):
            mq[i] = ultimo_contenedor
            espacio_contenedor -= W[i]
        else:
            ultimo_contenedor += 1
            mq[i] = ultimo_contenedor
            espacio_contenedor = C -W[i] #

    return mq


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    espacio_contenedor = [C] * len(W) # Lista de contenedores sera igual a la longitud de la lista usar como java no con append
    pqq = []  # Aqui podemos utilizar append
    for i in range (len(W)):
        #print(W[i])
        for contenedor in range(len(espacio_contenedor)):

            if W[i] <= espacio_contenedor[contenedor]:
                pqq.append(contenedor)
                espacio_contenedor[contenedor] -=W[i]
                break
    return pqq


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:

    indices_ordenados = sorted(range(len(W)), key=lambda i: -W[i])

    print(indices_ordenados)
    espacio_contenedor = [C] * len(W)  # Lista de contenedores sera igual a la longitud de la lista usar como java no con append
    pqqo = [-1] * len(W)  # Aqui podemos utilizar append
    for i in indices_ordenados:  # asd
        # print("Indice i: "+str(i))
        for contenedor in range(len(espacio_contenedor)):
            # print("contenedor: "+str(contenedor))
            if W[i] <= espacio_contenedor[contenedor]:
                # print("W[i] <= espacio_contenedor[contenedor]: ")
                # print(str(W[i])+" "+str(espacio_contenedor[contenedor]))
                # print("pqqo[i] = contenedor: ")
                # print(str(pqqo[i])+" "+str(contenedor))
                pqqo[i] = contenedor
                # print("espacio_contenedor[contenedor] -= W[i]")
                # print(str(espacio_contenedor[contenedor])+" "+str(W[i]))
                espacio_contenedor[contenedor] -= W[i]
                break
    return pqqo


def prueba_binpacking():
    W: List[int] = [1, 2, 8, 7, 8, 3]
    C: int = 10

    for solve in [mientras_quepa, mientras_quepa_V2 ,primero_que_quepa, primero_que_quepa_ordenado]:
        sol = solve(W, C)
        print("-" * 40)
        print("Método:", solve.__name__)
        if len(sol) == 0:
            print("No implementado")
        else:
            print("Solución: {}, usados {} contenedores\n".format(sol, 1 + max(sol)))


if __name__ == "__main__":
    prueba_binpacking()