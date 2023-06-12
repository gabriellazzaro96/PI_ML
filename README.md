# PROYECTO INDIVIDUAL N°1
## Machine Learning Operations (MLOps)
### *Sistema de recomendación de películas*

## Resumen
El siguiente proyecto se basa en dos partes. En primer lugar, se realizó un sistema de consultas para obtener información vinculada a películas, como popularidad, directores, actores y fechas. En segundo lugar, mediante un modelo de Machine Learning, se desarrolló un sistema de recomendación de películas basado en un título ingresado por el usuario, el cual devuelve un listado de 5 películas similares.

## Herramientas
- :snake: [Python](https://docs.python.org/): Lenguaje de programación utilizado en el proyecto.
- :panda_face: [Pandas](https://pandas.pydata.org/): Biblioteca de manipulación y análisis de datos.
- :1234: [NumPy](https://numpy.org/doc/): Biblioteca para cálculos numéricos en Python.
- :gear: [scikit-learn](https://scikit-learn.org/stable/): Biblioteca de aprendizaje automático en Python.
- :rocket: [FastAPI](https://fastapi.tiangolo.com/): Framework web para el desarrollo de APIs en Python.
- :unicorn_face: [Uvicorn](https://www.uvicorn.org/): Servidor ASGI de alto rendimiento para aplicaciones web en Python.
- :computer: [Streamlit](https://docs.streamlit.io/): Biblioteca para la creación de aplicaciones web interactivas en Python.

## Recomendaciones previas
- Escribir todo en minúscula.
- No usar caracteres especiales.

## Contexto y Rol
Se trabajó simulando ser un Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. Partimos desde cero con dos conjuntos de datos con poca madurez, a los cuales se les tuvo que realizar un trabajo fino de Ingeniería de datos. Esto mismo se puede observar en el archivo ETL.py, donde se podrán encontrar tareas como fusión de conjuntos de datos, eliminación de columnas con poca información, conversión en el tipo de datos, eliminación y completado de datos nulos, desanidado de columnas, entre otras tareas. Las principales herramientas utilizadas para esto fueron :snake: Python, :panda_face: Pandas y :1234: NumPy.

Una vez con la fuente de datos limpia, ordenada y disponible, se procedió a desarrollar una API que cuenta con seis endpoints, de los cuales se puede extraer información útil e interesante del mundo cinematográfico:
- :calendar: cantidad_filmaciones_mes: Nos devuelve información sobre la cantidad de películas estrenadas en el número de mes que ingresemos.
- :calendar: cantidad_filmaciones_dia: Nos devuelve información sobre la cantidad de películas estrenadas en el número de mes que ingresemos.
- :bar_chart: score_titulo: Nos devuelve el año de estreno y el score asignado al título de la película que introduzca el usuario.
- :bar_chart: votos_titulo: Nos devuelve la cantidad de votos asignados y un promedio de la valuación del título ingresado, siempre y cuando tenga más de 2000 votos.
- :bust_in_silhouette: get_actor: Nos devuelve el éxito del actor ingresado por el usuario, las películas en las que participó y un promedio del retorno obtenido por estas.
- :bust_in_silhouette: get_director: Nos devuelve el éxito del director obtenido a través del retorno de las películas que dirigió, además devuelve las películas que dirigió y información sobre las mismas.

El código de la API se encuentra en el archivo main.py. La misma fue desarrollada en :snake: Python utilizando :panda_face: Pandas y :rocket: FastAPI en conjunto con :unicorn_face: Uvicorn para su deployment. Se puede acceder a la misma mediante el siguiente link: [https://pi-mlo-gel.onrender.com/docs](https://pi-mlo-gel.onrender.com/docs)

Respecto al Sistema de Recomendación de películas, se basa en un modelo de aprendizaje automático (Machine Learning). Utiliza técnicas de procesamiento de texto y algoritmos de vecinos más cercanos para proporcionar recomendaciones de películas similares a partir de un título ingresado por el usuario.

Su funcionalidad es la siguiente:
- Prepara los datos seleccionando las columnas relevantes y combinándolas en una sola columna llamada "features".
- Crea una matriz TF-IDF utilizando el vectorizador de :gear: scikit-learn para representar numéricamente la importancia de cada palabra en el contexto de todas las películas.
- Construye un modelo de vecinos más cercanos basado en la distancia del coseno y el algoritmo de fuerza bruta.
- Implementa la función get_recommendations para obtener recomendaciones de películas similares a partir de un título de película ingresado.
- Configura la interfaz de usuario con :computer: Streamlit para permitir al usuario ingresar un título de película y obtener recomendaciones similares.

El código proporciona una forma interactiva de explorar y descubrir nuevas películas basadas en recomendaciones generadas por el modelo.

Se puede acceder al mismo mediante el siguiente link: [https://gabriellazzaro96-pi-ml-ml-gabi-8gho5e.streamlit.app/](https://gabriellazzaro96-pi-ml-ml-gabi-8gho5e.streamlit.app/)

## Video tutorial
Aquí iría mi video, si tuviera uno.

## Contacto
- Gmail: gabriellazzaro96@gmail.com
- GitHub: [https://github.com/gabriellazzaro96](https://github.com/gabriellazzaro96)
