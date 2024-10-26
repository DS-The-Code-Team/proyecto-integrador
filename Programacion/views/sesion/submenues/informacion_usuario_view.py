import os

def informacion_usuario_view():
    print(f"""
            Nombre y apellido: {os.getenv('nombre_inversor')} {os.getenv('apellido_inversor')}\n
            Correo: {os.getenv('correo_inversor')}\n
            CUIL: {os.getenv('cuil_inversor')}\n
            Fecha de registro: {os.getenv('fecha_registro_inversor')}\n
        """)