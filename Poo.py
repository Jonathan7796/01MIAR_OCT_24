class Estudiante : #Pascal case para clases en Python
    
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def Estudiar(self):
        print("Estudiando...")

nombre = input("Digame su nombre:")
edad = input("Ingrese su edad:")
grado = input("Ingrese su grado:")

pedro = Estudiante("Pedro",12,"5to")    
  