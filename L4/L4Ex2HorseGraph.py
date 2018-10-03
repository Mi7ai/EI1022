from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from Utils.graph2dviewer import Graph2dViewer

def horse_graph(rows, cols):

    aristas = []
    saltos = [(1,-2), (2,-1), (2,1), (1,2)]
    for r in range(rows):
        for c in range(cols):
            for (ri, ci) in saltos:
                    if r+ri < rows and 0 <= c+ci < cols:
                        aristas.append( ((r,c),(r+ri,c+ci)))

    return UndirectedGraph(E=aristas)
#Acabar
def numero_casillas_alcanzables(grafo,vertices) -> int:

    pass
#Acabar
def matriz_saltos(grafo,num_rows,num_cols):
    m = []
    #Generar una matriz
    for r in range(num_rows):
        m.append([0] * num_cols)

    #deep_copy para copiar matrices o con un for

    #TODO
    #copiar el codigo del recorredor de aristas en anchura y
    # modificarlo para rellenar a la vez matriz m

    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((0, 0))
    seen.add((0,0))
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))

    return m
def recorredor_aristas_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<(T,T)>":
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))
    seen.add(v_inicial)
    while len(queue)>0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas
if __name__ == '__main__':

    num_rows = 8
    num_cols = 8
    grafo_tablero = horse_graph(num_rows,num_cols)

    print(numero_casillas_alcanzables(grafo_tablero,(0,3)))
    viewer = Graph2dViewer(grafo_tablero, window_size=(400,400))
    viewer.run()