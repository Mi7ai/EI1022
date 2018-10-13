import sys
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from labyrinthviewer import LabyrinthViewer


def load_labyrinth(nombre_fichero):
    vertices = set()
    f = 0  # f = fila
    for linea in open(nombre_fichero):
        celdas = linea.split(',')
        for c in range(len(celdas)):  # c = columna
            muro = celdas[c]  # contiene info de donde estan los muros,wsn,se,etc...

            if 's' not in muro:
                vertices.add(((f, c), (f + 1, c)))
            if 'n' not in muro:
                vertices.add(((f, c), (f - 1, c)))
            if 'e' not in muro:
                vertices.add(((f, c), (f, c + 1)))
            if 'w' not in muro:
                vertices.add(((f, c), (f, c - 1)))

        f += 1

    return UndirectedGraph(E=vertices)


def create_matriz(rows, cols): #Crea matriz de costes a -1

    matrix = [[-1] * cols for y in range(rows)]

    return matrix

def recorredor_aristas_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<(T, T)>": #este metodo hay que retocarlo para modificar la matriz de costes
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


def path(g, source, target):
    # Step 1
    la = recorredor_aristas_anchura(g, source)

    # Step 2
    parent = {}
    for (u, v) in la:
        parent[v] = u

    # Step 3
    camino = []

    v = target
    camino.append(v)
    while parent[v] != v:
        v = parent[v]
        camino.append(v)

    # Step 4
    return camino


if __name__ == '__main__':
    lab = load_labyrinth(sys.argv[1])

    source = (0, 0)
    rec = recorredor_aristas_anchura(lab, source)

    t, target = rec[-1]

    # lab = UndirectedGraph(E=v)
    print(lab)

    camino = path(lab, source, target)

    v = LabyrinthViewer(lab, canvas_width=400, canvas_height=400)
    v.set_input_point(source)
    v.set_output_point(target)
    v.add_path(camino, 'blue')
    v.run()
