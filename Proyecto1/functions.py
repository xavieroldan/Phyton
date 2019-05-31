#definir una función
# se hacen antes del main

def sayMyName ():
    name = input("Cuál es tu nombre?")
    print("Hola "+name)

def getMyName ():
    name = input("Cuál es tu nombre?")
    return name

def multTen():
    num = input("Dame un número:")
    output = float(num) * 10
    return output

if __name__ == '__main__':

    #sayMyName()

    #print("Cojo de getMyName: "+ getMyName())


    print("Y el número es: "+ str(multTen()))

