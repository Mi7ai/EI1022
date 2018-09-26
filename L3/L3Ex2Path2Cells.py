from Utils.labyrinthviewer import LabyrinthViewer
from L3.L3Ex1CreateLabyrinth import create_labyrinth
import random


def recorredor_aristas_profundidad(grafo: "Graph<T>", v_inicial: "T") -> "List<(T,T)>":
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(v,suc)


    # aristas.append((u,v))
    aristas = []
    seen = set()
    recorrido_desde(v_inicial, v_inicial)
    return aristas

def path(g, source, target):
# Step 1
    la = recorredor_aristas_profundidad(g,source)

#Step 2
    parent = {}
    for (u, v) in la:
        parent[v] = u

#Step 3
    camino = []

    v = target
    camino.append(v)
    while parent[v] != v:
        v = parent[v]
        camino.append(v)

#Step 4
    return camino
#Labyrinth viewer
# ---> MAIN PROGRAM <---
if __name__ == '__main__':
    random.seed(7)




    rows = 40
    cols = 40
    lab = create_labyrinth(40, 40)

    source = (0,0)
    target = (rows-1, cols-1)
    camino = path(lab, source, target)
    viewer = LabyrinthViewer(lab, canvas_width=800, canvas_height=480, margin=10)
    viewer.add_path(camino)
    viewer.run()