if __name__ == '__main__':

    print("Vamos a probar cosas!")
    print("=====================")

    name = input("Nombre?")
    job = input("Ocupación?")
    age = int(input("Edad?"))

    if age >= 18:
        print(name+": eres mayor de edad y tu profesión es "+ job)
    else:

        if age <= 5:
            print("Eres un bebé")

                    

        else:
            a = 18 - age
            print("Lo siento: "+ name+ ": no puedes trabajar de "+ job+ " porque no eres mayor de edad. Te faltan "+ str(a) +" años.")