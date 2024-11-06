from views.menu_basico_view import menu_basico_view
from models.transaccion import Transaccion
from dao.accion_dao import AccionDAO
from dao.inversor_dao import InversorDAO
from dao.transaccion_dao import TransaccionDAO
from utils.loggin_colors import log_info, log_error, log_warning
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


def __accion_seleccionada_precio(id_accion, acciones):
    position = id_accion - 1
    log_info(f"acción elegida, {acciones[position]}")
    accion = acciones[position]
    return accion[2]
            

def __actualizar_saldo():
    dao_inversor = InversorDAO()
    saldo_usuario = dao_inversor.get_saldo(os.getenv('id_inversor'))
    os.environ['saldo_inversor'] = str(saldo_usuario)


def __validacion_saldo(operacion, precio, cantidad):
    if operacion == 'compra':
        saldo_usuario = float(os.getenv('saldo_inversor'))
        if saldo_usuario < (precio * cantidad):
            log_error("Saldo insuficiente.")
            return False
        else:
            return True
        

def __validacion_input_numero(msj, maximo=1000):
    while True:
            try:
                numero = int(input(msj))
                if numero <= 0 or numero > maximo:
                    print("Por favor, ingrese un número valido.")
                    continue
                if isinstance(numero, int):
                    return numero
            except ValueError:
                print("Por favor, ingrese un número válido.")
                

def __actualizar_acciones_mercado(dao_accion, id_accion, cantidad_mercado):
    dao_accion.update_accion(id_accion, cantidad_mercado)


def __validacion_compra_cantidad(cantidad, data_accion):
    while cantidad > data_accion.cantidad_mercado:
        log_warning("No hay suficientes acciones en el mercado.")
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


def __resumen_transaccion(id_accion, cantidad, data_accion, saldo_usuario, precio_compra):
    print(f"""
            Acción seleccionada: {id_accion}
            Cantidad seleccionada: {cantidad}
            Cantidad disponible: {data_accion.cantidad_mercado}
            Costo unitario: ${precio_compra}
            Costo total: ${cantidad * precio_compra} 
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
            print(f"ID: {id_accion}, Nombre: {nombre_accion}, Precio de compra: ${precio_compra}, cantidad en mercado: {cantidad_mercado}")
        print("")
        
        id_accion = __validacion_input_numero("Ingrese el ID de la acción que desea comprar: ",int(acciones[-1][0]))
        cantidad = __validacion_input_numero("Ingrese la cantidad de acciones que desea comprar: ")
        
        precio_compra = __accion_seleccionada_precio(id_accion, acciones)

        data_accion = accion_dao.get(id_accion)
        
        __resumen_transaccion(id_accion, cantidad, data_accion, saldo_usuario, precio_compra)

        cantidad = __validacion_compra_cantidad(cantidad, data_accion)

        saldo_suficiente = __validacion_saldo('compra', precio_compra, cantidad)

        if saldo_suficiente:
                
            continuar_comprando = __confirmar()

            if continuar_comprando:
                transacciones_dao = TransaccionDAO()
                exito_compra = transacciones_dao.comprar_accion(id_usuario, id_accion, cantidad)

                if exito_compra:
                    __actualizar_saldo()
                    __actualizar_acciones_mercado(accion_dao, id_accion, data_accion.cantidad_mercado - cantidad)
                    print(f"Compra realizada con éxito.\nSu saldo actual es ${saldo_usuario}\n")
                    break
                else:
                    log_error("Error en la compra. Verifique su saldo o datos.")
                    break
        
        else:
            print(f"Compra cancelada por saldo insuficiente.\n")
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
        """ 
--------------------------------------------------------------- ACA DEJE --------------------------------------- """
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
