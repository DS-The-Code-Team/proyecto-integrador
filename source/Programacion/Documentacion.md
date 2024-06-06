# Documentación del Desarrollo de diagrama de clases para ARGBroker Demo

## Introducción
En este documento se describe el desarrollo del diagrama de clases para el área de programación

## Tareas
- Identificación de clases 
- Creación de clases
- Establececimiento de relaciones
- Realizar diagrama de clases
- Documentar diagrama

Las tareas se dividieron por igual entre el equipo

## Nomenclatura
Las clases se nombran utilizando la metodología PascalCase, y los atributos y métodos la de snake_case
No se usan tildes, ñ ni carácteres especiales en la definición de nombres

## Clases

INVERSOR

Atributos público
id_usuario: string » identificación del usuario 
id_cuenta: int » identificación de la cuenta de cliente del usuario 

Atributos privados   
nombre: string
email: string
telefono: int
contrasena: string 

Métodos privados
- set_usuario(id_usuario, nombre,email,contraseña): datos_usuario: list » Definición de los valores del usuario, se asignan por parámetros del método y la función retorna una lista con los valores nuevos
- cambiar_contrasena(datos_usuario, contrasena_nueva: string)
- crear_cuenta_cliente(datos_usuario, id_cuenta): dict
- acceder_datos_usuario(id_usuario): dict
- iniciar_session_cuenta_cliente(id_usuario | id_cuenta, contrasena): bool
- cerrar_sesion_cuenta_cliente(id_usuario): bool