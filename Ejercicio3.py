class calculadora:
    def __init__(self) :
        self.valor1=int(input("Ingrese primer valor " ))
        self.valor2=int(input("Ingrese segundo valor " ))

    def mostrar(self):
        print("Valor1: ",self.valor1)
        print("Valor2: ",self.valor2)

    def suma(self):
        self.adición=self.valor1+self.valor2
        print("El resultado de la suma es ", self.adición)

    def resta(self):
        self.sustracción=self.valor1-self.valor2
        print("El resultado de la resta es ", self.sustracción)  

    def multiplicación(self):
        self.timez=self.valor1*self.valor2
        print("El resultado de la multiplicación es ", self.timez)  

    def division(self):
        self.divided=self.valor1/self.valor2
        print("El resultado de la division es ", self.divided) 


operación=calculadora()
operación.mostrar()
operación.suma()
operación.resta()
operación.multiplicación()
operación.division()