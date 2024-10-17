
#Modelamos entidad Inversor - Usuario
class Inversor:
    def __init__(self, id: int, nombre: str, apellido: str, cuil: int, correo: str, contrasena: str, pin: int, saldo=1000000.00):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.correo = correo
        self.contrasena = contrasena
        self.pin = pin
        self.saldo = saldo