# Twikit Tweet Collector

Esta aplicación recopila todos los tweets de un usuario específico utilizando la biblioteca Twikit y los almacena en una lista. La aplicación maneja la paginación y evita la duplicación de tweets ya vistos.

## Requisitos

- Python 3.7+
- Biblioteca Twikit

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

   2. Instala las dependencias:
       ```sh
       pip install twikit
       ```

## Configuración

1. Actualiza las credenciales de usuario en el archivo `app.py`:

        ```python
        USERNAME = 'USUARIO'
        EMAIL = 'EMAIL'
        PASSWORD = 'CONTRASEÑA'
        ```

## Uso

1. Ejecuta la aplicación:
        ```sh
        python app.py
        ```

2. La aplicación iniciará sesión en Twikit, obtendrá todos los tweets del usuario especificado (`elonmusk` en este caso) y los imprimirá en la consola.