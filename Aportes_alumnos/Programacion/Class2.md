

## BD: corresponde a Compra y Venta
**Class: Broker**  
*Attributes*  
_broker_name: string  
_broker_commission: number(float)  
  
*Méthods*  
get_broker_name(): string  
get_broker_comission(): number(float)  
<br />

**Class: Operation**  
*Attributes*  
#id_operation: string  
#quantity: number(int)  
#price: number(float)  
#commission: number(float)  
#type: string <!-- compra o venta -->  
  
*Méthods*  
_set_id_operation(): string  
_get_broker_comission(): number(float) <!-- obtiene porcentaje de comisión del broker  -->  
_set_comission(): number(float) <!-- calculo de porcentaje de la comisión sobre el precio y retorna el valor en pesos -->  
<br />

**Class: Buy**  
*Attributes*  
id_buy: string  
_summary_buy: dict   
  
*Méthods*  
_set_id_buy(): string  <!-- modifica el id_buy con el id_operation -->  
_set_summary_buy(): dict <!-- claves y valores con id_buy + quantity, price, comission y type de superclase Operaction -->  
get_summary_buy(): dict  
<br />

**Class: Sell**  
*Attributes*  
id_sell: string  
_summary_sell: dict   

*Méthods*  
_set_id_sell(): string  <!-- modifica el id_sell con el id_operation -->  
_set_summary_sell(): dict <!-- claves y valores con id_sell + quantity, price, comission y type de superclase   Operaction -->  
get_summary_sell(): dict  
<br />

## BD: corresponde a Transaccion
**Class: Transaction**   
*Attributes*  
id_transaction: string  
_user: string  
_company_stock: string  
_id_buy: string | null » sí es compra hay string, sino es null  
_id_sell: string | null » ""  
_date: string  
<br />

*Méthods*  
_get_id_transaction(): string  
_get_user(): string  
_get_company_stock(): string  
_check_transaction(): string <!-- evalua sí la transacción es de compra o venta y retorna el la operación y el id correspondiente -->  
_get_date(): string  
summary(): string <!-- crea un comprobante con un resumen de los datos anteriores -->  
<br />


## BD: corresponde a Portafolio
**Class: Portfolio**  
*Attributes*  
_id_portfolio: string  
_user: string  
_company_stocks: dict <!-- acciones y cantidad -->  
_committed_value: number(float)  
  
*Méthods*  
get_id_portfolio(): string  
get_company_stocks(): dict  
set_company_stocks(): dict  
get_committed_value(): number(float)  
<br />

