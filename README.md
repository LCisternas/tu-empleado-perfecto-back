# Backend aplicacion Tu empleado perfecto
## Aplicacion desarrollada con Django, Django rest framework y MySql alojando la base de datos en PlanetScale

> Acciones necesarias para ejecutar el codigo localmente
* Configurar entorno virtual
* Instalacion de paquetes [django, django_restframework, django_filters, corsheader, drf_yasg, python-dotenv]
* El proyecto fue desarrollado utilzando MySql como base de datos, es posible configurar una localmente, pero el proyecto considera el uso del servicio cloud PlanetScale, y viene configurado para su uso, las credenciales deben ser extraidas desde un archivo .env

> Se recomienda ejecutar los comandos de inicio en este orden
* python3 manage.py makemigrations
* python3 manage.py migrate
* python3 manage.py createsuperuser
* python3 manage.py runserver

> El desarrollo de la API tambien cuenta con documentacion automatica se puede acceder a ella mediante la siguiente url
* localhost/api/docs
