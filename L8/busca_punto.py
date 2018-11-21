
def busca_punto_rec(v):
    def rec(b: int, e:int ):
        if e-b == 0: return None
        h = (b+e)//2
        if v[h] < h:
            return rec(h,e)
        elif v[h] > h:
            return rec(b,h)
        else:
            return h
    return rec(0, len(v))

#para acasa hacrlo sin recursividad

# def busca_punto_fijo(v):
#     def rec(b: int, e:int ):
#        #cond de parada del while if e-b == 0: return None
#
#        #dentro del while
#        h = (b+e)//2
#         if v[h] < h:
#             return rec(h,b)
#         elif v[h] > h:
#             return rec(b,h)
#         else:
#             return h
#         #hasta aqui
#     return rec(0, len(v))

def busca_punto_pico(v):
    def rec(b: int, e: int):
        if e-b == 1: return b
        h = (b+e)//2 #mitad
        if v[h] <= h:
            return rec(h, e)
        return rec(b,h)
    return rec(0, len(v))

if __name__ == "__main__":
    v = [-10, -5, 1, 15, 3, 6]
    print(busca_punto_pico(v))