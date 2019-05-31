#definir una función
# se hacen antes del main

def sayMyName ():
    name = input("Cuál es tu nombre?")
    print("Hola "+name)

def getMyName ():
    name = input("Cuál es tu nombre?")
    return name

if __name__ == '__main__':

    sayMyName()

    print("Cojo de getMyName: "+ getMyName())

