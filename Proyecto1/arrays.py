if __name__ == '__main__':

    # lista.append(10)  # añadimos datos
    # lista.append(25)
    # lista.append(-3)
    # lista.append(15)
    #
    # print(lista[3])  # leemos datos
    #
    # print(len(lista))  # da la longitud
    #
    # lista.pop()  # borra la última posición de de la lista
    #
    # lista.insert(2, "hola")



    # guardamos las palabras creadas por el usuario

    lista = [] # declaramos la lista
    word = ""

    print("Escribe lo que quieras y pulsa enter.")
    print("=====================================")
    print("Escribe \"salir\" para salir")

    while word.lower() != "salir":

        word = input("Escribe la palabra:")
        lista.append(word)

    lista.pop()

    # Recorrer la lista y sacar cada línea por pantalla


    for i in range(0, len(lista)):

        print("Posición "+str(i)+" está la palabra: "+ lista[i])

    print("FIN")

    for palabra in lista : print(palabra) # recorre el array y lo imprime completo














