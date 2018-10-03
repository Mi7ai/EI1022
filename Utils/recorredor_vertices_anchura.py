from algoritmia.datastructures.queues import Fifo


def recorredor_vertices_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<T>":
    vertices = []
    queue = Fifo()
    seen = set()
    queue.push(v_inicial)
    seen.add(v_inicial)
    while len(queue) > 0:
        v = queue.pop()
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
    queue.push(suc)
    return vertices

