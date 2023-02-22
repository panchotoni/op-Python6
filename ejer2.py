class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        if (self.nota >= 6) and (self.nota < 11):
            print("Usted ", self.nombre, " aprobo la materia con: ", self.nota)
        elif (self.nota < 6) and (self.nota >= 0):
            print("Usted desaprobo")
        else:
            print("El valor no es valido")

rosti = Alumno("Bautista Rostand", 8)
rosti.aprobo()