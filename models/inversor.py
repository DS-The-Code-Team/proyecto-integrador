#Modelamos entidad Inversor - Usuario
class Inversor:
    def __init__(self, nombre: str, apellido: str, cuil: int, correo: str, contraseña: str, pin: int, saldo=1000000.00):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.correo = correo
        self.contraseña = contraseña
        self.pin = pin
        self.saldo = saldo