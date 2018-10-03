from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues.fifo import Fifo

import random

"CREATE LABYRINTH MODIFICATION"


def create_labyrinth(rows: int, cols: int, n: int = 0) -> UndirectedGraph:
    # Definition

    # Step 1
    vertices = [(r, c) for r in range(rows) for c in range(cols)]

    # Step 2
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)


    # Step 3
    edges = []
    for (r, c) in vertices:
        if r + 1 < rows:
            edges.append(((r, c), (r + 1, c)))
        if c + 1 < cols:
            edges.append(((r, c), (r, c + 1)))
    random.shuffle(edges)

    # Step 4
    corridors = []
    discarted_edges = []  #modificacion


    # Step 5
    for (u, v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        else:
            discarted_edges.append((u, v))  #modificacion

    corridors.extend(discarted_edges[:n])  #modificacion

    # Step 6
    return UndirectedGraph(E=corridors)


def recorredor_aristas_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<(T, T)>":
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))
    seen.add(v_inicial)

    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas


def recuperador_camino(lista_aristas,v):

    bp = {}
    for o, d in lista_aristas:
        bp[d] = o
    # Reconstruye el camino yendo hacia atrás
    camino = []
    camino.append(v)
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    # Invierte el camino pues lo hemos obtenido al revés
    camino.reverse()
    return camino


# Labyrinth viewer
# ---> MAIN PROGRAM <---
if __name__ == '__main__':
    random.seed(42)

    # Crear el laberinto con num_paredes_quitadas

    num_rows = 80
    num_cols = 140
    num_paredes_quitadas = 20
    celda_entrada = (0, 0)
    celda_salida = (num_rows - 1, num_cols - 1)

    lab = create_labyrinth(num_rows, num_cols, num_paredes_quitadas)

    # Obtenemos la lista de arista de un recorrido de anchura desde (0,0)
    lista_aristas = recorredor_aristas_anchura(lab, celda_entrada)

    # Recuperamos el camino desde la salida con backpointers
    camino = recuperador_camino(lista_aristas, celda_salida)

    #print(lab)

    viewer = LabyrinthViewer(lab, canvas_width=800, canvas_height=480, margin=10)
    viewer.add_path(camino, 'blue')
    viewer.run()
