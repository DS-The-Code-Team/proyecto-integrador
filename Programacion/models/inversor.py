
#Modelamos entidad Inversor - Usuario
class Inversor:
    def __init__(self, nombre: str, apellido: str, cuil: int, correo: str, contrasena: str, pin: int, saldo:float, id_usuario: int = None, fecha_alta: str = None):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.correo = correo
        self.contrasena = contrasena
        self.pin = pin
        self.saldo = saldo      
        self.id = id_usuario
        self.fecha_alta = fecha_alta

"""     
    @staticmethod
    def registrar_inversor_view():
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        cuil = int(input("Ingrese CUIL: "))
        correo = input("Ingrese email: ")
        contrasena = input("Ingrese contraseña: ")
        pin = int(input("Ingrese pin: "))
        saldo = 1000000.00
        # Crear una instancia de Inversor con los datos ingresados
        nuevo_inversor = Inversor(id=0, nombre=nombre, apellido=apellido, cuil=cuil, correo=correo, contrasena=contrasena, pin=pin, saldo=saldo)
        return nuevo_inversor
    
    # Ejemplo de uso en main.py
    nuevo_inversor = Inversor.registrar_inversor_view()
    print(f"Inversor registrado: {nuevo_inversor.nombre} {nuevo_inversor.apellido}")

 """