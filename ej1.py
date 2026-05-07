

class Alumnos : 
    def __init__(self, nombre, edad, curso, apellido) :
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def mostrar(self) :
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Curso: ", self.curso)
        
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese la edad: ")
curso = input("Ingrese el curso: ")


alumno1 = Alumnos(nombre, apellido, edad, curso)

alumno1.mostrar()