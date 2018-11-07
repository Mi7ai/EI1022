import sys
from typing import Tuple, List, Type

Folleto = [int, int, int]
PosicionFolleto = []


def lee_fichero_imprenta(fichero):
    Folletos = []

    f = open(fichero)
    tamaño_hoja = f.readline()

    # print(tamaño_hoja)

    for linea in f:
        infoFolleto = linea.split(" ")
        # creamos el folleto
        Folletos.append((int(infoFolleto[0]), int(infoFolleto[1]), int(infoFolleto[2])))

    # print(Folletos)
    return tamaño_hoja, Folletos


# devuelve Trus si se ha podido hacer la resta, sino False
def restar(anchura_folleto, altura_folleto, anchura_hoja, altura_hoja, indice_hoja, l):
    if anchura_hoja - anchura_folleto >= 0 and altura_hoja - altura_folleto >= 0:
        #return ((anchura_hoja - anchura_folleto), (altura_hoja - altura_folleto))
        return True
    # if l[indice_hoja][0] - anchura_hoja - anchura_folleto < 0 or l[indice_hoja][1] - altura_hoja - altura_folleto < 0:
    #     return -2
    return False


def optimiza_folletos(m, folletos):
    # ordenamos por el area del folleto(base x altura)
    # folletos_ordenados = sorted(folletos, key=lambda folletos: folletos[1] * folletos[2])
    # print(folletos_ordenados)

    # ordenamos los indices de los folletos para que nos devuelvan de mayor a mayor altura
    folletos_ordenados = sorted(folletos, key=lambda folletos: -(folletos[2]))
    print(folletos_ordenados, end=" ")
    print()

    espacio_paginas = [(int(m), int(m))] * len(
        folletos)  # lista con tamaño=folletos_ordenados y rellena del tamaño de hoja
    l = [int(m), int(m)] * len(folletos)  # Aqui podemos utilizar append

    for indice_folleto in folletos_ordenados:
        num_folleto = indice_folleto[0]
        anchura_folleto = indice_folleto[1]
        altura_folleto = indice_folleto[2]
        xA = 0
        yA = 0
        for indice_hoja in range(len(espacio_paginas)):  # devuelve la tupla con el tamaño en cada hoja
            anchura_hoja = espacio_paginas[indice_hoja][0]
            altura_hoja = espacio_paginas[indice_hoja][1]
            #if folletos_ordenados[indice_folleto] < espacio_paginas[indice_hoja][0]:

            # devuelve true si se ha posido hacer la resta | false si no se cabe en la hoja
            #resta = restar(anchura_folleto, altura_folleto, anchura_hoja, altura_hoja, indice_hoja,l)  # devuelve la resta o -1 si no se cabe en la hoja

            #if resta:  # el folleto cabe en la hoja y en resta tenemos la tupla del tamaño de hoja que queda por rellenar
                # lo metemos en la hoja y actualizamos valores de la hoja
                # añado al indice de la pagina

             #   pos_x = resta[0]  # lo que actualmente hemos restado 30
             #    pos_y = resta[1]  # lo que actualmente hemos restado 30

            xA = xA + anchura_folleto  # valor de anchura acumulado 0+30
            yA = yA + altura_folleto  # valor de altura acumulado 0+30


            print(xA, end=" ")
            print(num_folleto, end=" ")
            print(anchura_folleto, end=" ")
            print(altura_folleto, end=" ")
            print("-", end=" ")

            PosicionFolleto.append((num_folleto, indice_hoja + 1, anchura_folleto, altura_folleto))
                # actualizar espacio_paginas para cambiar el tamaño de la x&y en la posicion de la hoja
                #l[indice_folleto] = ((pos_x), (pos_y))
            # romper cuando a l la resta le de por debajo de 0 - para cambiar de hoja
            if xA >= anchura_hoja or yA >= altura_hoja:  #es cuando rompemos
                break
    return PosicionFolleto


def muestra_solucion(solucion):
    print()
    for f in sorted(solucion):
        # print("hola", end=" ")
        # print(str(f[0])+" "+str(f[1])+" "+str(f[2])+" "+str(f[3])+" ")
        print('{} {} {} {}'.format(f[0], f[1], f[2], f[3]))


if __name__ == '__main__':
    tam_hoja, Folletos = lee_fichero_imprenta(sys.argv[1])
    lista = optimiza_folletos(tam_hoja, Folletos)
    muestra_solucion(lista)
