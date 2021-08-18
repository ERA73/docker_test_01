# Pasos para montar Django y Redis en Docker (UBUNTU 20.04)

## **DJango:**
### **Preparar el proyecto**
* Desde la carpeta default(~) clonar el repositorio https://github.com/ERA73/docker_test_01.git
	* git clone https://github.com/ERA73/docker_test_01.git hacker_news

* crear el archivo de docker Dokerfile
	* cd ~/hacker_news/app/pruebadkr
	* nano Dokerfile
```
# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.4-slim

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
# RUN apt install pipenv && pipenv shell
RUN apt-get update
RUN apt install -y \
                gcc \
                gettext \
#               mysql-client libmysqlclient-dev \
#               postgresql-client libpq-dev \
                sqlite3 \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]
```

* Instalar pipenv
	* sudo apt install pipenv
	* cd ~/hacker_news/app
	* pipenv install

* activar el entorno virtual
	* pipenv shell

* instalar las dependencias
	* cd ~/hacker_news/app/pruebadkr
	* pip install -r requirements.txt

* ejecutar las migraciones
	* python manage.py migrate

### **Montar el contenedor con Django**
* docker build -t python-django-app .
### **Ejecutar el contenedor**
* docker run -it -p 80:80 python-django-app

## **Redis**

* Crear carpeta db
	* mkdir db
	* cd db
	* nano Dockerfile
```
FROM        ubuntu:20.04
RUN         apt-get update && apt-get install -y redis-server
EXPOSE      6379
ENTRYPOINT  ["/usr/bin/redis-server"]
```

* construir el contenedor
	* docker build -t root/redis .

* ejecutar redis en el contenedor
	* docker run -d --name redis -p 6379:6379 root/redis

### **Validar Redis**
* ejecutar el cliente de redis
	* docker exec -it redis redis-cli