class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
 
    
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
 

class Empleado(Persona):

    def __init__(self):
       
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
 

    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
 
 

    def pagar_impuestos(self):
        if self.sueldo > 3600000:
            self.descuento= int((self.descuento/100)*3.5)
            self.total= int((self.sueldo-self.descuento))
        else:
            print("El empleado no paga impuestos.")
            self.descuento=0
            self.total=self.sueldo

    def descuento_(self):
        print("el descuento equivale a ",self.descuento)    
        print("el sueldo del empleado equivale a",self.total)    

 

persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()
empleado1.descuento_()
