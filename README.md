# Prueba-api-git

API REST desarrollada con FastAPI que obtiene la información de un usuario GitHub autenticado, con 
una arquitectura monolitica de capas.

## Tecnologías
- Python 3.12
- FastAPI
- Requests

## Instalación

```bash
git clone https://github.com/mateocar/Prueba-api-git.git
cd Prueba-api-git.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Ejecutar el proyecto
uvicorn app.main:app --reload
