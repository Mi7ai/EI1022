def busca(v):
    def rec(b: int, e: int):
        if e-b == 1: return b
        h = (b+e)//2 #mitad
        mejorder = rec(b,h)
        mejoriz = rec(h, e)
        mejorM = 0 #while del medio
        return max(mejoriz,mejorder,mejorM)
    return rec(0, len(v))