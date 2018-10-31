from Utils.bt_scheme import PartialSolution, BacktrackingSolver
from typing import *
from copy import deepcopy

Position = Tuple[int, int]
Sudoku = List[List[int]]


def primera_vacia(s: Sudoku) -> Optional[Position]:
    for fila in range(9):
        for col in range(9):
            if s[fila][col] == 0:
                return fila, col
    return None  # si el Sudoku ya está completo

def vacias(s: Sudoku)-> List[Position]:
    return [(fila, col) for fila in range(9) for col in range(9)if s[fila][col] == 0] #lo mismo que arriba mas o menos solo que devuelve la lista vacia si cumple el if


def posibles_en(s: Sudoku, fila: int, col: int) -> Set[int]:
    used = set(s[fila][c] for c in range(9))
    used = used.union(s[f][col] for f in range(9))
    fc, cc = fila // 3 * 3, col // 3 * 3
    used = used.union(s[fc + f][cc + c] for f in range(3) for c in range(3))
    return set(range(1, 10)) - used


def pretty_print(s: Sudoku):
    for i, fila in enumerate(s):
        for j, columna in enumerate(fila):
            print(columna if columna != 0 else ' ', end="")
            if j in [2, 5]:
                print("|", end="")
        print()
        if i in [2, 5]:
            print("---+---+---")


class SudokuPS(PartialSolution):
    def __init__(self, sudoku: Sudoku, vacias: List[Position]):
        self.vacias = vacias
        self.s = sudoku
        sn = deepcopy(self.s)

    # Indica si la sol. parcial es ya una solución factible (completa)
    def is_solution(self) -> bool:
        # return primera_vacia(self.s) is None
        return len(vacias(self.s)) == 0

    # Si es sol. factible, la devuelve. Si no lanza excepción
    def get_solution(self) -> Sudoku:
        # if not self.is_solution(): raise RuntimeError("No hay solucion!")
        if self.is_solution() == False:
            raise RuntimeError("No hay solucion!")
        return self.s

    # Devuelve la lista de sus sol. parciales sucesoras
    def successors(self) -> Iterable["SudokuPS"]:
        # pos = primera_vacia(self.s)
        # if pos is None: return
        # f, c = pos
        #
        # for num in posibles_en(self.s, f, c):
        #     sudoku_nuevo = deepcopy(self.s)
        #     sudoku_nuevo[f][c] = num
        #     yield SudokuPS(sudoku_nuevo)
        # -------------------------
         mejor_pos = argmin(self.vacias, lambda pos: len(posibles_en(self.s, pos[0], pos[1])))
        # esto se cambbia por pos de arriba y se añaden las 2 lineas de vacias_nueva
        # -------------------------
        if mejor_pos(self.s) is None: return
        f, c = mejor_pos
        vacias_nueva = deepcopy(self.vacias)
        vacias_nueva.remove(mejor_pos)
        for num in posibles_en(self.s, f, c):
                sudoku_nuevo[f][c] = num
                yield SudokuPS(sudoku_nuevo,vacias)
        sudoku_nuevo[f][c] = 0
        self.vacias.append(mejor_pos)

# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    m_sudoku = [[0, 0, 0, 3, 1, 6, 0, 5, 9], [0, 0, 6, 0, 0, 0, 8, 0, 7], [0, 0, 0, 0, 0, 0, 2, 0, 0],
                [0, 5, 0, 0, 3, 0, 0, 9, 0], [7, 9, 0, 6, 0, 2, 0, 1, 8], [0, 1, 0, 0, 8, 0, 0, 4, 0],
                [0, 0, 8, 0, 0, 0, 0, 0, 0], [3, 0, 9, 0, 0, 0, 6, 0, 0], [5, 6, 0, 8, 4, 7, 0, 0, 0]]

    # El sudoku más difícil del mundo
    #m_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
    #            [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
    #            [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    print("Original:")
    pretty_print(m_sudoku)
    print("\nSoluciones:")
    # Mostrar todas las soluciones
    # IMPLEMENTAR utilizando SudokuPS y BacktrackingSolver

    initial_ps = SudokuPS(m_sudoku) # objeto que solo usa los 3 metodos de arriba
    for solution in BacktrackingSolver.solve(initial_ps):
        pretty_print(solution)
    print("<TERMINDADO>")  # Espera a ver este mensaje para saber que el programa ha terminado
