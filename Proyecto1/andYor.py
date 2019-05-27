if __name__ == '__main__':

    age = int(input("Edad?"))

    if age < 12:
        print("Eres niño")

    elif age > 12 and age <21:
        print("Eres un adolescente")

    else:
        print("Eres un adulto")
