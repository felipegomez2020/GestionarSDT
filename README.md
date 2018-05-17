# GestionarProyect

Gestoinar es un proyecto ----- que corre bajo la version de python ****

## Caracteristicas

- Modo desarrollo configuracion principal, que permite desplegar en servidor de pruebas
- Base de datos SQLITE, configuracion de archivos estaticos finalizados
- Heroku(En proceso)

## ¿Como iniciar?

Para usar este proyecto es necesario realizar los siguientes pasos.

1. Instalacion de python en la version 2.7, configuracion de variables de entorno.
2. Instalacion de dependencias mediante comando python pip install -r requirements.txt,
   para instalar estos complementos debe estar ubicado en la carpeta donde esta el archivo mencionado.
3. Preparar migraciones a la BD mediante el comando python manage.py makemigrations
4. Realizar migraciones a la BD mediante el comando python manage.py migrate
5. creacion de superusuario para el administrador mediante el comando python manage.py createsuperuser
   y llenar los correspondientes datos.
  

## Ejercutar proyecto

Para Ejercutar este proyecto localmente es realmente facil:

    python manage.py runserver 0.0.0.0:8000


# ara ejecutar los comandos que usan el archivo python manage.py es necesario ubicarse en la carpeta raiz de este archivo.
