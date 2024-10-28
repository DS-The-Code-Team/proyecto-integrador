from views.menu_basico_view import menu_basico_view
from models.transaccion import Transaccion
from dao.accion_dao import AccionDAO
from dao.transaccion_dao import TransaccionDAO
import os 

def comprar_acciones_view():
    while True:
        continuar = input("¿Desea comprar acciones? (s para continuar, n para volver atrás): ")
        if continuar.lower() != 's':
            print("Volviendo al menú anterior...")
            return

        id_usuario = os.getenv('id_inversor')
        saldo_usuario = os.getenv('saldo_inversor')

        accion_dao = AccionDAO()
        acciones = accion_dao.get_precios_de_acciones()

        if not acciones:
            print("No hay acciones para comprar")
            return
        
        print("Acciones disponibles:")
        for id_accion, nombre_accion, precio_compra in acciones:
            print(f"ID: {id_accion}, Nombre: {nombre_accion}, Precio de compra: {precio_compra}")

        volver_atras = input("¿Desea volver atrás? (s para volver, cualquier otra tecla para continuar): ")
        if volver_atras.lower() == 's':
            print("Volviendo al menú anterior...")
            return

        id_accion = input("Ingrese el ID de la acción que desea comprar: ")
        cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))

        transacciones_dao = TransaccionDAO()
        exito_compra = transacciones_dao.comprar_accion(id_usuario, id_accion, cantidad)

        if exito_compra:
            print(f"Compra realizada con éxito.\n Su saldo actual es ${saldo_usuario}")
        else:
            print("Error en la compra. Verifique su saldo o datos.")
        
        volver_atras = input("¿Desea seguir comprando? (s/n): ")
        if volver_atras.lower() != 's':
            break

def vender_acciones_view():
    while True:
        continuar = input("¿Desea vender acciones? (s para continuar, n para volver atrás): ")
        if continuar.lower() != 's':
            print("Volviendo al menú anterior...")
            return

        id_usuario = os.getenv('id_inversor')
        saldo_usuario = os.getenv('saldo_inversor')

        accion_dao = AccionDAO()
        acciones_portafolio = accion_dao.get_acciones_portafolio(id_usuario)

        if not acciones_portafolio:
            print("No tienes acciones para vender.")
            return
        
        print("Acciones disponibles en su portafolio:")
        for id_accion, nombre_accion, cantidad_acciones in acciones_portafolio:
            print(f"ID: {id_accion}, Nombre: {nombre_accion}, Cantidad: {cantidad_acciones}")

        volver_atras = input("¿Desea volver atrás? (s para volver, cualquier otra tecla para continuar): ")
        if volver_atras.lower() == 's':
            print("Volviendo al menú anterior...")
            return    

        id_accion = input("Ingrese el ID de la acción que desea vender: ")
        cantidad = int(input("Ingrese la cantidad de acciones que desea vender: "))

        transacciones_dao = TransaccionDAO()
        exito_venta = transacciones_dao.vender_accion(id_usuario, id_accion, cantidad)

        if exito_venta:
            print(f"Venta realizada con éxito.\n Su saldo actual es ${saldo_usuario}")
        else:
            print("Error en la venta. Verifique sus datos o la cantidad de acciones a vender.")
        
        volver_atras = input("¿Desea seguir vendiendo? (s/n): ")
        if volver_atras.lower() != 's':
            break

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
