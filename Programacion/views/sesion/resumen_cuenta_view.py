# Crear interfaz de resumen: saldo inicial o actual, historial de transacciones y rendimiento de inversiones
import os
def resumen_cuenta_view():
    print(f"""Hola {os.environ['nombre_inversor']} {os.environ['apellido_inversor']}, este es tu resumen de cuenta: \n
          Saldo actual: ${os.environ['saldo_inversor']}\n
          Rendimiento de inversions: 0%\n
          """)
   
    
     