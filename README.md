# curso_fastapi_pro
Curso de Udemy con mayor profundidad para crear apis: Crea APIs REST con FastAPI, autenticación segura, bases de datos y despliegue full stack listo para producción


### Empezamos con el uso de UV
#### 1. Crear repo / iniciar proyecto
uv init

#### 2. Crear venv (opcional, uv lo crea automáticamente al añadir deps)
uv venv **(--python 3.11) Se puede espeficicar la version por mas que no la tengas instalada

#### 3. Añadir dependencias
uv add fastapi uvicorn etc...

#### 4. Lock + sync
uv lock # genera/actualiza uv.lock
uv sync # instala las dependencias en el .venv (según uv.lock)

uv add modifica pyproject.toml y uv lock genera uv.lock. uv sync sincroniza el entorno con el lockfile. uv run también fuerza lock+sync automáticos antes de ejecutar un comando.  

##### 5. Ejecutar (uv run asegura que se use el entorno correcto)
uv run python -m uvicorn main:app --reload o uv run python -m uvicorn main.py

#### 6. Exportar requirements.txt
uv pip compile pyproject.toml -o requirements.txt

# Objetivo del Curso:
Este curso tiene como meta que aprendas a desarrollar APIs RESTful modernas, seguras y listas para producción utilizando FastAPI, uno de los frameworks más eficientes del ecosistema Python. A lo largo de la formación, dominarás técnicas de autenticación y autorización con JWT, integración con bases de datos relacionales mediante SQLAlchemy, y despliegue de proyectos full stack en entornos reales. También te entrenarás en el uso de buenas prácticas, arquitectura limpia, pruebas automatizadas y documentación interactiva con Swagger. El objetivo final es que seas capaz de crear y mantener sistemas backend profesionales, listos para escalar.  

&nbsp;
# Aca Empezamos otro curso ya que el de Udemy era una estafa, todo texto sin ejercicios y hecho por IA. A partir de aca Empezamos a seguir 2 cursos de Youtube
1. https://www.youtube.com/watch?v=O23LpHEQHhw&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=4
2. https://www.youtube.com/watch?v=UI48zzl2TBU&list=PL2PZw96yQChzll2RHgViiQ8eUvIQycAVl
