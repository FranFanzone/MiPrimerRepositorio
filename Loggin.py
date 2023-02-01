def loggin(datoslogg):
    nombre_usuario=input('Ingrese su nombre de usuario: ')
    contrasena=input('Ingrese su contrasena: ')    
    datoslogg.update({nombre_usuario:contrasena})
    return datoslogg