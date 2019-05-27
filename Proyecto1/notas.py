"""Pedimos 3 notas del 0 al 10.
Si la media es >5 aprobado. si no suspendido"""

if __name__ == '__main__':

    nota1 = float(input("Nota 1?"))
    nota2 = float(input("Nota 2?"))
    nota3 = float(input("Nota 3?"))

    avg = (nota1+nota2+nota3)/3

    if avg <5:
        print("Has suspendido.")

    elif avg >= 5 and avg <6:
        print("Suficiente: aprobado por los pelos!")

    elif avg >=6 and avg <7:
        print("Has sacado un bien.")

    elif avg >=7 and avg <9:
        print("Has sacado un notable")

    else:
        print("Excelente!")

    print("Tu media es de :" + str(avg))