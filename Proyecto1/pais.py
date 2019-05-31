# me pida el nombre de un pais
# me imprimer le nombre de un pais

def setCountry():
    return input("Dame el país")

def printCountry(input):
    print("El país es "+ input)

if __name__ == '__main__':

        country = setCountry()
        printCountry(country)
