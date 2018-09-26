"""
    def ___len(self)___ modifica el metodo original de python
    def ___iter(self)___ modifica el metodo original de python [ for i in instancia ]
    def ___str(self)___ el to string de java, comodo para los humanos
    def ___repr(self)___ solo se usa si def ___iter(self)___ no esta definido [ crean un str y lo devuelven ]. comodo
        para el ordenador.
    def ___lt(self,other)___ si existe se puede hacer la comparacion de: a < b
    def ___call(self, *args)___ hacer que un metodo haga una llamada!?, ana(param)

    Propriedades:
    print(a.x) es igual a a.get()
    a.x = 5 es igual a a.set(5)

    Dependencias: si no se inserta un parametro cuando se instancia la clase se usa el constructor por defecto, si se le
    pone parametro se usa el constructor que se le pasa a la clase

    Excepciones: raise IndexError("mensaje")

    Yield: importante
"""