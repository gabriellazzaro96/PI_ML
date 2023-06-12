import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import streamlit as st

# Cargar el dataset
data = pd.read_csv('datasets/movies_clean.csv')

data = data[['title', 'belongs_to_collection', 'original_language', 'genres', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'cast', 'director']]

# Combinar las características en una sola columna
data['features'] = data.apply(lambda x: ' '.join(x.values.astype(str)), axis=1)

# Crear la matriz TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['features'])

# Creamos el modelo de vecinos más cercanos
knn = NearestNeighbors(metric='cosine', algorithm='brute')
# Entrenamos el modelo
knn.fit(tfidf_matrix)

def get_recommendations(title, knn_model, data, num_recommendations=5):
    # Obtener el índice de la película que coincide con el título
    idx = data[data['title'] == title].index[0]

    # Encontrar los vecinos más cercanos
    distances, indices = knn_model.kneighbors(tfidf_matrix[idx], n_neighbors=num_recommendations+1)

    # Obtener los índices de las películas más similares (excluyendo la película de consulta)
    movie_indices = indices.flatten()[1:]

    # Devolver las películas recomendadas
    return data['title'].iloc[movie_indices]

# Configurar la interfaz de usuario con Streamlit
st.title('Recomendaciones de películas')
st.write('Ingrese el título de una película para recibir recomendaciones similares.')

movie_title = st.text_input('Título de la película')

if st.button('Obtener recomendaciones'):
    if movie_title:
        recommendations = get_recommendations(movie_title, knn, data)

        st.subheader(f'Recomendaciones para "{movie_title}":')
        st.write(recommendations)
    else:
        st.write('Por favor, ingrese un título de película.')

