**Class: Transaction** 
*Attributes*
id_transaction: string
_user: string
_company_stock: string
_id_buy: string | null » sí es compra hay string, sino es null
_id_sell: string | null » ""
_date: string

*Méthods*
_get_id_transaction(): string
_get_user(): string
_get_company_stock(): string
_check_transaction(): string <!-- evalua sí la transacción es de compra o venta y retorna el la operación y el id correspondiente -->
_get_date(): string
summary(): string <!-- crea un comprobante con un resumen de los datos anteriores -->


<!-- BD: corresponde a Compra y Venta -->

**Class: Operation**
#quantity: number(int)
#price: number(float)
#commission: number(float)
#type: string <!-- compra o venta -->

*Méthods*
get_broker_comission(): number(float) <!-- obtiene porcentaje de comisión del broker  -->
set_comission(): number(float) <!-- calculo de porcentaje de la comisión sobre el precio y retorna el valor en pesos -->


**Class: Buy** 
*Attributes*
id_buy: string




Venta
  ID_venta
  Cant_venta
  Precio_venta 
--- Comision_venta
+++ Comision_broker

Portafolio
  ID_portfolio
  ID_usuario
  ID_acción
  Cant_acciones
  Valor_comprometido

Broker
	Nombre
	Comision
