class Calculadora:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    def sumar(self):
        resultado = self.numero1 + self.numero2
        return resultado

    def dividir(self):

        if float(self.numero2) != 0:
            output = float(self.numero1) / float(self.numero2)

        else:
            output = "No puedes dividir entre cero"

        return output