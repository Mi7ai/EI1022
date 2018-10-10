import sys

from algoritmia.datastructures.digraphs import UndirectedGraph
import labyrinthviewer
def load_labyrinth(nombre_fichero):
    vertices = set()
    f = 0  # f = fila
    for linea in open(nombre_fichero):
        celdas = linea.split(',')
        for c in range(len(celdas)):  # c = columna
            muro = celdas[c]  # contiene info de donde estan los muros,wsn,se,etc...

            if 's' not in muro:
                vertices.add(((f + 1), (c)))
            if 'n' not in muro:
                vertices.add(((f - 1), (c)))
            if 'e' not in muro:
                vertices.add((f, (c + 1)))
            if 'w' not in muro:
                vertices.add((f, (c - 1)))

    f += 1

    return UndirectedGraph(vertices)




if __name__ == '__main__':
    lab = load_labyrinth(sys.argv[1])
    print(lab)

    viewer = Labyrinthviewer(lab, canvas_width=800, canvas_height=480, margin=10)
    viewer.run()
