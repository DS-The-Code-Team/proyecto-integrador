*Pasos git*

*_Inicio y Agregar repositorio_*
	git init
	git remote add origin https://github.com/DS-The-Code-Team/proyecto-integrador.git
	git fetch 
	git pull origin main


*_Antes de iniciar algún cambio_*
» Es importante para descargar los cambios que otros hayan hecho
	git fetch 
	git pull origin main


*_Para subir cambios_*
» el . agrega todos los cambios
	git add .
	git commit -m "mensaje corto y representativo del cambio entre comillas"
	git push u origin main
