from dao.inversor_dao import InversorDAO

def login_inversor_view():
    dao = InversorDAO()
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    dao.get_login(correo, contrasena)