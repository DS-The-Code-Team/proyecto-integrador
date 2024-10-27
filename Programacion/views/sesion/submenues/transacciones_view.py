from views.menu_basico_view import menu_basico_view
from models.transaccion import Transaccion
from dao.accion_dao import AccionDAO
from dao.transaccion_dao import TransaccionDAO
import os 


def comprar_acciones_view():
    while True:  
        # Obtenemos datos de usuario de las variables de entorno
        id_usuario = os.getenv('id_inversor')
        saldo_usuario = os.getenv('saldo_inversor')

        # Listado de acciones a elegir para comprar
        accion_dao = AccionDAO()
        acciones = accion_dao.get_precios_de_acciones()  # Lista

        if not acciones:
            print("No hay acciones para comprar")
            return
        
        # Mostrar acciones disponibles con su precio de compra
        print("Acciones disponibles:")
        for id_accion, nombre_accion, precio_compra in acciones:
            print(f"ID: {id_accion}, Nombre: {nombre_accion}, Precio de compra: {precio_compra}")

        # Opción de volver atrás
        volver_atras = input("¿Desea volver atrás? (s para volver, cualquier otra tecla para continuar): ")
        if volver_atras.lower() == 's':
            print("Volviendo al menú anterior...")
            return  # Regresar sin hacer nada

        # Solicitar al usuario que ingrese la acción y la cantidad
        id_accion = input("Ingrese el ID de la acción que desea comprar: ")
        cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))

        transacciones_dao = TransaccionDAO()
        exito_compra = transacciones_dao.comprar_accion(id_usuario, id_accion, cantidad)

        if exito_compra:
            print(f"Compra realizada con éxito.\n Su saldo actual es ${saldo_usuario}")
        else:
            print("Error en la compra. Verifique su saldo o datos.")
        
        # Opción de volver atrás
        volver_atras = input("¿Desea seguir comprando? (s/n): ")
        if volver_atras.lower() != 's':
            break  # Salir del bucle si el usuario no quiere seguir comprando

        

def vender_acciones_view():
    while True:  #Bucle para gestionar decisiones de usuario

        # Preguntar al usuario si quiere comprar o salir
        continuar = input("¿Desea comprar acciones? (s para continuar, n para volver atrás): ")
        if continuar.lower() != 's':
            print("Volviendo al menú anterior...")
            return  # Regresar sin hacer nada

        # Obtenemos datos de usuario de las variables de entorno
        id_usuario = os.getenv('id_inversor')
        saldo_usuario = os.getenv('saldo_inversor')

        # Listado de acciones en el portafolio del usuario
        accion_dao = AccionDAO()
        acciones_portafolio = accion_dao.get_acciones_portafolio(id_usuario)  # Método que deberías implementar para obtener acciones del portafolio

        if not acciones_portafolio:
            print("No tienes acciones para vender.")
            return
        
        # Mostrar acciones disponibles en su portafolio con su cantidad
        print("Acciones disponibles en su portafolio:")
        for id_accion, nombre_accion, cantidad_acciones in acciones_portafolio:
            print(f"ID: {id_accion}, Nombre: {nombre_accion}, Cantidad: {cantidad_acciones}")

        # Opción de volver atrás
        volver_atras = input("¿Desea volver atrás? (s para volver, cualquier otra tecla para continuar): ")
        if volver_atras.lower() == 's':
            print("Volviendo al menú anterior...")
            return  # Regresar sin hacer nada    

        # Solicitar al usuario que ingrese la acción y la cantidad a vender
        id_accion = input("Ingrese el ID de la acción que desea vender: ")
        cantidad = int(input("Ingrese la cantidad de acciones que desea vender: "))

        transacciones_dao = TransaccionDAO()
        exito_venta = transacciones_dao.vender_accion(id_usuario, id_accion, cantidad)

        if exito_venta:
            print(f"Venta realizada con éxito.\n Su saldo actual es ${saldo_usuario}")
        else:
            print("Error en la venta. Verifique sus datos o la cantidad de acciones a vender.")
        
        # Opción de volver atrás
        volver_atras = input("¿Desea seguir vendiendo? (s/n): ")
        if volver_atras.lower() != 's':
            break  # Salir del bucle si el usuario no quiere seguir vendiendo





def transacciones_historial():
    print("Historial de transacciones")


def transacciones_view():
    submenu_title = "Menú Transacciones"
    submenu_opciones = {
        "1": ("Compra", comprar_acciones_view),
        "2": ("Venta", vender_acciones_view),
        "3": ("Historial", transacciones_historial),
        "4": ("Volver al menú anterior", None),
    }

    menu_basico_view(submenu_title, submenu_opciones)