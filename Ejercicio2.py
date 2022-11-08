class alumno:
    def __init__(self) :
       self.nombre=input("Ingrese nombre:")
       self.nota=int(input("Ingrese nota:"))

    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nombre",self.nota)

    def aprobación(self):
        if self.nota>3:
            print("Aprobo")
        elif self.nota<3:
            print("No Aprobo")
        else:
            print("valor no valido")            

estudiante=alumno()
estudiante.mostrar()
estudiante.aprobación()
