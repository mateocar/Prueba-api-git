# Prueba-api-GitHub

API REST desarrollada con **FastAPI** que obtiene información de un usuario **GitHub autenticado**, incluyendo repositorios, organizaciones y pull requests.  
El proyecto utiliza una **arquitectura monolítica simple por capas**.

---

## Arquitectura

La aplicación sigue una **arquitectura en capas simple**:

- **Capa API / Controller**: definición del endpoint con FastAPI (`main.py`)
- **Capa de Servicio**: consumo de la API de GitHub (`service.py`)
- **API Externa**: GitHub REST API
  
---

##  Reproducibilidad

Pasos necesarios para clonar, configurar y ejecutar el proyecto en un entorno local.

### Requisitos previos

- Python 3.12 o superior
- Git
- Cuenta de GitHub con un **Personal Access Token**

## Tecnologías

- Python 3.12
- FastAPI
- Uvicorn
- Requests
- python-dotenv

## Clonar el repositorio

```bash
git clone https://github.com/mateocar/Prueba-api-git.git
cd Prueba-api-git
```
## Crear entorno virtual
python -m venv venv

Activar el entorno virtual

Windows
```
venv\Scripts\activate
```

Linux / Mac
```
source venv/bin/activate
```
Instalar dependencias
```
pip install -r requirements.txt
```
## Generación del token de GitHub

Para consumir la API de GitHub es necesario generar un **Personal Access Token**.

### Pasos:

1. Ingresar a GitHub y acceder a:
   - **Settings → Developer settings → Personal access tokens**
2. Seleccionar **Tokens (classic)**.
3. Hacer clic en **Generate new token**.
4. Asignar un nombre descriptivo al token.
5. Seleccionar los siguientes permisos:
   - `repo`
   - `read:org`
6. Generar el token y **copiarlo**.

## Configurar variables de entorno
    
Crear un archivo .env en la raíz del proyecto:

    GITHUB_TOKEN=tu_personal_access_token
    
 Importante:

  - El token define qué usuario se consulta
  - Si el token no es válido o no existe, la API retornará un error
  - No se debe modificar el código para cambiar de usuario

Ejecutar el proyecto
```
uvicorn app.main:app --reload
```
La API estará disponible en:

http://127.0.0.1:8000

Documentación interactiva

FastAPI genera automáticamente documentación interactiva con Swagger:

http://127.0.0.1:8000/docs


Desde esta interfaz se puede probar el endpoint directamente.
Endpoint disponible

- GET /github-info

Este endpoint retorna:

- Repositorios del usuario autenticado
- Organizaciones del usuario
- Pull Requests creados por el usuario

### Notas
- El proyecto no utiliza base de datos.
- La información se obtiene directamente desde la API de GitHub.


