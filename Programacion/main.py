from dao.inversor_dao import InversorDAO
from models.inversor import Inversor
import logging

logging.basicConfig(level=logging.INFO)

#Consola, vistas:   

def registrar_inversor_view():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cuil = input("Ingrese CUIL: ")
    correo = input("Ingrese email: ")
    contrasena = input("Ingrese contraseña: ")
    pin = input("Ingrese pin: ")
    saldo = 1000000.00

    inversor = Inversor(nombre, apellido, cuil, correo, contrasena, pin, saldo)
    dao = InversorDAO()
    dao.create(inversor)
  

def listar_inversores_view():
    dao = InversorDAO()
    inversores = dao.get_all()
    for inversor in inversores:
        print(inversor)

def login_inversor_view():
    dao = InversorDAO()
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    dao.login(correo, contrasena)




# Ejecución del menú o las vistas
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Registrar inversor")
    print("2. Listar inversores")
    print("3. Login inversor")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_inversor_view()
    elif opcion == "2":
        listar_inversores_view()
    elif opcion == "3":
        login_inversor_view()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")