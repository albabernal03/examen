
class Libro():
    def __init__(self,nombrelibro, codigo, fecha_prestamo, fecha_devolucion, nombre_lector):
        self.nombrelibro = nombrelibro
        self.codigo = codigo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.nombre_lector = nombre_lector

    def setnombrelibro(self,nombrelibro):
        self.nombrelibro= nombrelibro

    def getnombrelibro(self):
        return self.nombrelibro

    def setcodigo(self,codigo):
        self.codigo= codigo

    def getcodigo(self):
        return self.codigo
    
    def setfecha_prestamo(self,fecha_prestamo):
        self.fecha_prestamo= fecha_prestamo

    def getfecha_prestamo(self):
        return self.fecha_prestamo

    def setfecha_devolucion(self,fecha_devolucion):
        self.fecha_devolucion= fecha_devolucion

    def getfecha_devolucion(self):
        return self.fecha_devolucion
    
    def setnombrelector(self,nombre_lector):
        self.nombre_lector= nombre_lector

    def getnombre_lector(self):
        return self.nombre_lector
      