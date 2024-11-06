from views.menu_basico_view import menu_basico_view
from models.transaccion import Transaccion
from dao.accion_dao import AccionDAO
from dao.inversor_dao import InversorDAO
from dao.transaccion_dao import TransaccionDAO
import os

def __confirmar():
    continuar = input(f"\n¿Desea continuar? (no para volver, si para continuar): ").lower().strip()
    if continuar == 'no':
        print("Volviendo al menú anterior...")
        return False
    elif continuar == 'si':
        print("")
        return True
    else:
        print("Opción inválida.")
        return __confirmar()
        

def __actualizar_saldo():
    dao_inversor = InversorDAO()
    saldo_usuario = dao_inversor.get_saldo(os.getenv('id_inversor'))
    os.environ['saldo_inversor'] = str(saldo_usuario)


def __actualizar_acciones_mercado(dao_accion, id_accion, cantidad_mercado):
    dao_accion.update_accion(id_accion, cantidad_mercado)


def __validacion_compra(cantidad, data_accion):
    while cantidad > data_accion.cantidad_mercado:
        print("No hay suficientes acciones en el mercado.")
        cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))
    if cantidad < data_accion.cantidad_mercado:    
        print(f"Costo total: ${cantidad * data_accion.precio_historico}")
        return cantidad

def __validacion_venta(cantidad, data_accion):
    while cantidad > data_accion.cantidad_acciones:
        print("No tienes suficientes acciones para vender.")
        cantidad = int(input("Ingrese la cantidad de acciones que desea vender: "))
    if cantidad < data_accion.cantidad_acciones:    
        return cantidad

def __resumen_transaccion(id_accion, cantidad, data_accion, saldo_usuario):
    print(f"""
            Acción seleccionada: {id_accion}
            Cantidad seleccionada: {cantidad}
            Cantidad disponible: {data_accion.cantidad_mercado}
            Costo unitario: ${data_accion.precio_historico}
            Costo total: ${cantidad * data_accion.precio_historico} 
            Saldo actual: ${saldo_usuario}
        """)

def comprar_acciones_view():
    continuar_comprando = True
    while continuar_comprando:
        
        id_usuario = os.getenv('id_inversor')
        saldo_usuario = os.getenv('saldo_inversor')

        accion_dao = AccionDAO()
        acciones = accion_dao.get_precios_de_acciones()

        if not acciones:
            print("No hay acciones para comprar")
            return
        

        print("Acciones disponibles:")
        for id_accion, nombre_accion, precio_compra, cantidad_mercado in acciones:
            print(f"ID: {id_accion}, Nombre: {nombre_accion}, Precio de compra: {precio_compra}, cantidad en mercado: {cantidad_mercado}")
        print("")

        id_accion = input("Ingrese el ID de la acción que desea comprar: ")
        cantidad = int(input("Ingrese la cantidad de acciones que desea comprar: "))

        data_accion = accion_dao.get(id_accion)
        
        __resumen_transaccion(id_accion, cantidad, data_accion, saldo_usuario)

        cantidad = __validacion_compra(cantidad, data_accion)
        continuar_comprando = __confirmar()

        if continuar_comprando:
            transacciones_dao = TransaccionDAO()
            exito_compra = transacciones_dao.comprar_accion(id_usuario, id_accion, cantidad)

            if exito_compra:
                __actualizar_saldo()
                __actualizar_acciones_mercado(accion_dao, id_accion, data_accion.cantidad_mercado - cantidad)
                print(f"Compra realizada con éxito.\n Su saldo actual es ${saldo_usuario}")
                break
            else:
                print("Error en la compra. Verifique su saldo o datos.")
                break


def vender_acciones_view():
    continuar_vendiendo = True
    while continuar_vendiendo:

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
        print("")

        
        id_accion = input("Ingrese el ID de la acción que desea vender: ")
        cantidad = int(input("Ingrese la cantidad de acciones que desea vender: "))

--------------------------------------------------------------- ACA DEJE ---------------------------------------
        data_portafolio = accion_dao.get_accion_portafolio(id_usuario)

        print(data_portafolio.cantidad_acciones)
        __confirmar()
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
