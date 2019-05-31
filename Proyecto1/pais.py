# me pida el nombre de un pais
# me imprimer le nombre de un pais

# def setCountry():
#     return input("Dame el país")
#
# def printCountry(input):
#     print("El país es "+ input)

#funcion suma: dado 2 números nos devuelve la suma de ambos

def suma(num1, num2):
    output = float(num1) + float(num2)
    return output

def div(num1, num2):

    if float(num2) != 0:
        output = float(num1) / float(num2)

    else:
        output = "No puedes dividir entre cero"

    return output



if __name__ == '__main__':
        #
        # country = setCountry()
        # printCountry(country)

#funcion suma: dado 2 números nos devuelve la suma de ambos

    # num1 = input("Dame un número para sumar:")
    # num2 = input("Dame otro número:")
    # result = suma(num1,num2)
    # print("La suma es: "+str(result))

    num1 = input("Dame un número para dividir:")
    num2 = input("Dame otro número:")
    result = div(num1,num2)
    print(result)



