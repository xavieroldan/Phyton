from Proyecto1.users import User


if __name__ == '__main__':

    user1 = User() # creo el objeto

    user1.nombre = "Xavi" #defino los atributos
    user1.edad = 42
    user1.email = "mimail@gmail.com"

    print(user1.nombre) #leo los atributos
