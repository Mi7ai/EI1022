import sys
from typing import Tuple

Folleto = Tuple[int, int, int]
PosicionFolleto = [int, int, int, int]


def lee_fichero_imprenta(fichero: str):
    folletos = []

    f = open(fichero)
    tamaño_hoja = f.readline()

    #print(tamaño_hoja)

    for linea in f:
        infoFolleto = linea.split(" ")
        #creamos el folleto
        folletos.append((int(infoFolleto[0]), int(infoFolleto[1]), int(infoFolleto[2])))

    print(folletos)
    return tamaño_hoja, folletos


def optimiza_folletos(m, folletos):
    folletos_ordenados = sorted(folletos, key=lambda folletos: folletos[1] * folletos[2])  ## Ordenamos por el area del folleto(base x altura)
    # print(folletos_ordenados)
    containers_freespace = [m, m] * len(folletos)
    res = [-1] * len(folletos)
    for num_object in folletos_ordenados:
        for num_container in range(len(containers_freespace)):
            if folletos[num_object] <= containers_freespace[num_container]:
                res[num_object] = num_container
                containers_freespace[num_container] -= folletos[num_object]
                break

    return res


# def muestra_solucion(solucion: List[PosicionFolleto]):
#   pass

if __name__ == '__main__':
    t, Folleto = lee_fichero_imprenta(sys.argv[1])
    res = optimiza_folletos(t, Folleto)
    print(res)
