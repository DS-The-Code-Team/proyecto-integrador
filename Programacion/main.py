from views.menu_inicio.menu_principal_view import mostrar_menu_principal_view
from views.sesion.pantalla_principal_view import sesion_pantalla_principal_view
import os

if __name__ == "__main__":  
    def usuario_existe():
        usuario = os.getenv("id_inversor")
        return usuario
    
    while True:
        usuario_logueado = usuario_existe()
        if not usuario_logueado: 
            mostrar_menu_principal_view()
        else:
            sesion_pantalla_principal_view()



       

     