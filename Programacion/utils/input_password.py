from bullet import Password

def input_password(msj):
    cli = Password(msj)
    contrasena = cli.launch()
    return contrasena