import sys
from algoritmia.datastructures.digraphs import UndirectedGraph
from labyrinthviewer import LabyrinthViewer


def load_labyrinth(nombre_fichero):
    vertices = set()
    f = 0  # f = fila
    for linea in open(nombre_fichero):
        celdas = linea.split(',')
        for c in range(len(celdas)):  # c = columna
            muro = celdas[c]  # contiene info de donde estan los muros,wsn,se,etc...

            if 's' not in muro:
                vertices.add(((f, c), (f+1, c)))
            if 'n' not in muro:
                vertices.add(((f, c), (f-1, c)))
            if 'e' not in muro:
                vertices.add(((f, c), (f, c + 1)))
            if 'w' not in muro:
                vertices.add(((f, c), (f, c - 1)))

        f += 1

    return UndirectedGraph(E=vertices)




if __name__ == '__main__':
    lab = load_labyrinth(sys.argv[1])
    print(lab)

    v = LabyrinthViewer(lab,canvas_width=400,canvas_height=400)
    v.run()
