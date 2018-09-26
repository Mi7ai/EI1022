from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.labyrinthviewer import LabyrinthViewer
from random import shuffle, randint

"""def gen(nr1,nr2):
    x, y = randint(nr1, nr2), randint(nr1, nr2)
print(next(gen(1,10)))"""

def create_labyrinth(rows, cols):
#Definition

#Step 1
    vertices = [(r, c) for r in range(rows) for c in range(cols)]

#Step 2
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)
#Step 3
    edges = []
    for (r, c) in vertices:
        if r+1 < rows:
            edges.append(((r, c), (r+1, c)))
        if c+1 < cols:
            edges.append(((r, c), (r, c+1)))
    shuffle(edges)

#Step 4
    corridors = []

#Step 5
    for (u,v) in edges:
       if mfs.find(u) != mfs.find(v):
           mfs.merge(u, v)
           corridors.append((u, v))

#Step 6
    return UndirectedGraph(E=corridors)










#Labyrinth viewer
#---> MAIN PROGRAM <---
if __name__ == '__main__':
    lab = create_labyrinth(40,40)
    print(lab)

    viewer = LabyrinthViewer(lab,canvas_width=800,canvas_height=480,margin=10)
    viewer.run()
