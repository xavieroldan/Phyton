from Proyecto1.users import User


if __name__ == '__main__':

    user1 = User("Xavi",42,"mimail@gmail.com") # creo el objeto llamando a la función del constructor

    print(user1.name) #leo los atributos

    user1.printAge()

    user2 = User("Pepito",56,"pepito@mail.com")

    user2.printAge()




