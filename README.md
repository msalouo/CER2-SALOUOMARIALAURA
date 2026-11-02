# Fundación Patrimonio Vivo

## 1. Descripción del proyecto

Fundación Patrimonio Vivo es una aplicación web desarrollada con Django que permite consultar un catálogo de lugares patrimoniales, visualizar sus detalles y filtrar por categorías.

El personal autorizado puede iniciar sesión y gestionar la información de los lugares patrimoniales según sus permisos.

## 2. Requisitos previos

Antes de instalar y ejecutar el proyecto, se deben tener las siguientes herramientas:

### Python

Se requiere tener instalado Python 3.

Para comprobar si está instalado, abrir una terminal (CMD o PowerShell) y ejecutar:

```bash
python --version
```

Si el comando no funciona, se debe descargar e instalar Python desde:

https://www.python.org/downloads/

Durante la instalación en Windows, se recomienda marcar la opción **Add Python to PATH**.

### pip

pip es el administrador de paquetes de Python y permite instalar Django y otras dependencias.

Comprobar su instalación con:

```bash
pip --version
```

### Git

Se necesita Git para descargar el repositorio desde GitHub.

Comprobar su instalación con:

```bash
git --version
```

Si no está instalado, descargar desde:

https://git-scm.com/downloads

### Django

Django es el framework utilizado para desarrollar la aplicación.

Una vez instalado Python y pip, se puede instalar Django mediante:

```bash
pip install django
```

Comprobar que Django quedó instalado:

```bash
python -m django --version
```

## 3. Instalación del proyecto

### 3.1 Descargar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd NOMBRE_DE_LA_CARPETA
```

## 4. Configuración de la base de datos

El proyecto utiliza SQLite, la base de datos predeterminada de Django.

Ejecutar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Crear usuario administrador

Para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Ingresar los datos solicitados para crear el usuario.

## 6. Ejecutar la aplicación

Iniciar el servidor local:

```bash
python manage.py runserver
```

Abrir el navegador e ingresar a:

http://127.0.0.1:8000/

## 7. Acceso al sistema

- **Inicio:** página principal de la fundación.
- **Catálogo:** permite consultar los lugares patrimoniales.
- **Categorías:** permite visualizar los lugares agrupados por categoría.
- **Detalles:** permite consultar la información completa de cada lugar.
- **Inicio de sesión:** permite ingresar al sistema según los permisos del usuario.
- **Administración:** http://127.0.0.1:8000/admin/
