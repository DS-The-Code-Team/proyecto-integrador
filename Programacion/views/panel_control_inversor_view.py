# # view/menu_control_inversor_view.py
# from view.inversor_cerrar_sesion_view import cerrar_sesion_view
# from view.menu_basico_view import menu_basico_view
# from view.listar_acciones_view import listar_acciones_view
# from dao.inversor_dao import InversorDAO

# def mostrar_panel_control_inversor_view(inversor_id):
#     dao = InversorDAO()
#     saldo, valor_comprometido, rendimiento_operacion = dao.obtener_datos_cuenta(inversor_id)
#     menu_control_title = "Panel de Control del Inversor"
#     menu_control_opciones = {
#         "1": ("Resumen de Cuenta", lambda: mostrar_resumen(saldo, valor_comprometido, rendimiento_operacion)),
#         "2": ("Acciones", listar_acciones_view),
#         "3": ("Cerrar Sesión", cerrar_sesion_view) 
#     }

#     menu_basico_view(menu_control_title, menu_control_opciones)

# def mostrar_resumen(saldo, valor_comprometido, rendimiento_operacion):
#     print("\n--- Resumen de Cuenta ---")
#     print(f"Saldo Actual: {saldo}")
#     print(f"Total Invertido: {valor_comprometido}")
#     print(f"Rendimiento Total: {rendimiento_operacion}")
#     input("Presione Enter para continuar...")
