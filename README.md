<div align="center">

![Logo de SoyHenry](images/logo_henry.png)
 
# PROYECTO INDIVIDUAL N°1 💻🎬
## Machine Learning Operations (MLOps)
### *Sistema de recomendación de películas* 🎥🍿

</div>

## Resumen 📜
El siguiente proyecto consta de dos partes. En primer lugar, se realiza un sistema de consultas para obtener información relacionada con películas, como popularidad, directores, actores y fechas, a partir de una base de datos de películas. En segundo lugar, se desarrolla un sistema de recomendación de películas basado en Machine Learning, el cual, a partir de un título ingresado por el usuario, devuelve un listado de 5 películas similares.

## Herramientas 🛠️
- :snake: [Python](https://docs.python.org/): Lenguaje de programación utilizado en el proyecto.
- :panda_face: [Pandas](https://pandas.pydata.org/): Biblioteca de manipulación y análisis de datos.
- :1234: [NumPy](https://numpy.org/doc/): Biblioteca para cálculos numéricos en Python.
- :gear: [scikit-learn](https://scikit-learn.org/stable/): Biblioteca de aprendizaje automático en Python.
- :rocket: [FastAPI](https://fastapi.tiangolo.com/): Framework web para el desarrollo de APIs en Python.
- :unicorn: [Uvicorn](https://www.uvicorn.org/): Servidor ASGI de alto rendimiento para aplicaciones web en Python.
- :computer: [Streamlit](https://docs.streamlit.io/): Biblioteca para la creación de aplicaciones web interactivas en Python.

## Recomendaciones previas ⚠️
- Escribir todo en minúscula.
- No utilizar caracteres especiales o acentuados.

## Contexto y Rol 📚👨‍💻
Se trabajó simulando ser un Data Scientist en una startup que provee servicios de agregación de plataformas de streaming. Se partió desde cero con dos conjuntos de datos con poca madurez, a los cuales se les realizó un trabajo exhaustivo de ingeniería de datos. Esto se puede observar en el archivo ETL.py, donde se llevaron a cabo tareas como la fusión de conjuntos de datos, eliminación de columnas con poca información, conversión de tipos de datos, eliminación y completado de valores nulos, y desanidado de columnas, entre otras. Las principales herramientas utilizadas para esto fueron :snake: Python, :panda_face: Pandas y :1234: NumPy.

Una vez que se tuvo una fuente de datos limpia, ordenada y disponible, se procedió a desarrollar una API que cuenta con seis endpoints de los cuales se puede extraer información útil e interesante sobre el mundo cinematográfico:

- :calendar: cantidad_filmaciones_mes: Devuelve información sobre la cantidad de películas estrenadas en el número de mes que se ingrese.
- :calendar: cantidad_filmaciones_dia: Devuelve información sobre la cantidad de películas estrenadas en el número de día que se ingrese.
- :bar_chart: score_titulo: Devuelve el año de estreno y el puntaje asignado al título de la película que ingrese el usuario.
- :bar_chart: votos_titulo: Devuelve la cantidad de votos asignados y el promedio de las valoraciones del título ingresado, siempre y cuando tenga más de 2000 votos.
- :bust_in_silhouette: get_actor: Devuelve el éxito del actor ingresado por el usuario, las películas en las que participó y un promedio del retorno obtenido por estas.
- :bust_in_silhouette: get_director: Devuelve el éxito del director a través del retorno de las películas que dirigió, además de información sobre las mismas.

El código de la API se encuentra en el archivo main.py y fue desarrollado en Python utilizando Pandas y FastAPI, en conjunto con Render para su implementación en producción. Se puede acceder a la API a través del siguiente enlace: [https://pi-mlo-gel.onrender.com/docs](https://pi-mlo-gel.onrender.com/docs))

Respecto al Sistema de Recomendación de películas, este se basa en un modelo de aprendizaje automático (Machine Learning). Utiliza técnicas de procesamiento de texto y algoritmos de vecinos más cercanos para proporcionar recomendaciones de películas similares a partir de un título ingresado por el usuario. 

Su funcionalidad se resume en los siguientes pasos:
1. Prepara los datos seleccionando las columnas relevantes y combinándolas en una sola columna llamada "features".
2. Crea una matriz TF-IDF utilizando el vectorizador de scikit-learn para representar numéricamente la importancia de cada palabra en el contexto de todas las películas.
3. Construye un modelo de vecinos más cercanos basado en la distancia del coseno y el algoritmo de fuerza bruta.
4. Implementa la función `get_recommendations` para obtener recomendaciones de películas similares a partir de un título de película ingresado.
5. Configura la interfaz de usuario con Streamlit para permitir al usuario ingresar un título de película y obtener recomendaciones similares.

El código proporciona una forma interactiva de explorar y descubrir nuevas películas basadas en recomendaciones generadas por el modelo. Se puede acceder al Sistema de Recomendación a través del siguiente enlace: [https://gabriellazzaro96-pi-ml-ml-gabi-8gho5e.streamlit.app/](https://gabriellazzaro96-pi-ml-ml-gabi-8gho5e.streamlit.app/)

## Video tutorial 🎥



## Contacto 📞
- Correo electrónico: gabriellazzaro96@gmail.com#da
- GitHub: [https://github.com/gabriellazzaro96](https://github.com/gabriellazzaro96)
