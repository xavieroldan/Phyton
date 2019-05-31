class User:
    def __init__(self, thisnName, thisAge, thisEmail):  # este es el constructor que se instancia vacío

        # definimos los atributos
        # self.nombre = "" # podemos poner "" o None
        # self.edad = None
        # self.email = None

        self.name = thisnName
        self.age = thisAge
        self.email = thisEmail

    def printAge(self):
        print("Tienes " + str(self.age) + " años.")

    def isPlus18(self):
        if self.age >= 18:
            output = "es mayor de edad"
        else:
            output = "no es mayor de edad"
        print(output)
