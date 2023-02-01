
def registro(datos):
    continuar=True
    continuar2=True
    while continuar:
        Usuario=input('Ingrese su nombre de usuario: ')
        if len(Usuario)<6:
            print('El nombre de usuario es demasiado corto, intentelo de nuevo.')
            Usuario=input('Ingrese su nombre de usuario: ')
        with open("C:/Users/franc/OneDrive/Escritorio/Python/Registro-Loggin/BD.txt", 'r') as BD:
            if Usuario in BD:
                print('Nombre de usuario no disponible.')
            else:
                print('Nombre de usuario aceptado.')
                continuar=False
    while continuar2:
        contrasena=input('Ingrese su contrasena: ')
        if len(contrasena)<6:
            print('La contrasena es demasiado corta, intentelo de nuevo.')
            contrasena=input('Ingrese su contrasena.')
        else:
            print('Contrasena aceptada.')
            print('Felicidades, has creado tu cuenta!')
            continuar2=False
    datos.update({Usuario:contrasena})
    return datos