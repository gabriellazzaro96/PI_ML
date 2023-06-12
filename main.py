from fastapi import FastAPI, Response
import pandas as pd
import json

#Instanciamos la app con FastAPI
app = FastAPI()

#Leemos el csv limpio
df = pd.read_csv("movies_clean.csv")

#Método que permite obtener la cantidad de peliculas estrenadas en el mes ingresdo
@app.get("/cantidad-filmaciones_mes/{mes}")
def get_cantidad_filmaciones_mes(mes: int):
    #Creamos un dataset nuevo aplicando el filtro del mes
    df1 = df[df['release_month'] == mes]
    #Obtenemos la cantidad de peliculas mediante el tamaño del dataset
    cantidad = df1.shape[0]
    #Creamos diccionario con la informacion requerida
    data = {
        "mes":mes,
        "peliculas": cantidad
    }
    # Convertimos el diccionario a JSON
    json_data = json.dumps(data, indent=4)    
    # Creamos la respuesta en JSON
    response = Response(content=json_data, media_type="application/json")
    return response

#Método que permite obtener la cantidad de peliculas estrenadas en el dia ingresdo
@app.get("/cantidad-filmaciones_dia/{dia}")
def get_cantidad_filmaciones_dia(dia: int):
    #Creamos un dataset nuevo aplicando el filtro del dia
    df1 = df[df['release_day'] == dia]
    #Obtenemos la cantidad de peliculas mediante el tamaño del dataset
    cantidad = df1.shape[0]
    #Creamos diccionario con la informacion requerida
    data = {
        "dia": dia,
        "peliculas": cantidad
    }
    # Convertimos el diccionario a JSON
    json_data = json.dumps(data, indent=4)    
    # Creamos la respuesta en JSON
    response = Response(content=json_data, media_type="application/json")
    return response

#Método que permite obtener el año de estreno y la popularidad de un titulo ingresado
@app.get("/score_titulo/{title}")
def get_score_titulo(title: str):
    # Creamos un dataset nuevo aplicando el filtro del titulo y que no este vacio
    df1 = df[df['title'].notna() & (df['title'] == title)]
    # Creamos diccionario con la informacion requerida
    data = {
        "titulo": df1["title"].tolist()[0],
        "año de estreno": df1["release_year"].tolist()[0],
        "puntaje": df1["popularity"].tolist()[0]
    }
    # Convertimos el diccionario a JSON
    json_data = json.dumps(data, indent=4)
    # Creamos la respuesta en JSON
    response = Response(content=json_data, media_type="application/json")
    return response

#Método que permite obtener la cantidad de votos de un titulo ingresado
@app.get("/votos_titulo/{title}")
def votos_titulo(title: str ):
    # Creamos un dataset nuevo aplicando el filtro del titulo, que no este vacio y que cumpla la condicion de mas de 2000 votos
    df1 = df[(df['title'].notna()) & (df['title'] == title) & (df['vote_count'] >= 2000)]
    # Condicional que devuelve un mensaje en caso de no alcanzar la cantidad minima de votos
    if df1.empty:
        return {'mensaje' : 'No posee la cantidad de votos minimos'}
    else:
        data = {
            "titulo": df1["title"].tolist()[0],
            "cantidad de votos": df1["vote_count"].tolist()[0],
            "promedio de votos": df1["vote_average"].tolist()[0]
        }
        # Convertimos el diccionario a JSON
        json_data = json.dumps(data, indent=4)    
        # Creamos la respuesta en JSON
        response = Response(content=json_data, media_type="application/json")
        return response         

# Método que permite obtener información sobre un actor ingresado        
@app.get("/actor/{actor}")
def get_actor_exito(actor: str):
    # Creamos un dataset nuevo aplicando el filtro del actor y que no este vacio
    df1 = df[df['cast'].notna() & df['cast'].str.contains(actor)]
    participaciones = df1.shape[0]
    retorno = df1['return'].sum()
    prom_retorno = retorno/participaciones    
    data = {
        'actor': actor,
        'exito': retorno,
        'participaciones': participaciones,
        'promedio del retorno':prom_retorno
    }
    # Convertimos el diccionario a JSON
    json_data = json.dumps(data, indent=4)
    # Creamos la respuesta en JSON
    response = Response(content=json_data, media_type="application/json") # Convert the data dictionary to a JSON string with proper indentation
    return response

# Método que permite obtener información sobre un director ingresado
@app.get("/director/{director}")
def get_director(director: str):
    # Creamos un dataset nuevo aplicando el filtro del director y que no este vacio
    df1 = df[df['director'].notna() & df['director'].str.contains(director)]
    # Sumamos los retornos del director
    retorno_dir = df1['return'].sum() 
    cantidad_peliculas = df1.shape[0]    
    data = {
        "director": director,
        "retorno del director": retorno_dir,
        "total de peliculas dirigidas": cantidad_peliculas,
        "peliculas": [{
            "titulo": df1["title"].tolist(),
            "estreno": df1["release_date"].tolist(),
            "retorno": df1["return"].tolist(),
            "presupuesto": df1["budget"].tolist(),
            "ganancias": df1["earns"].tolist(),
        }]
    }
    # Convert the data dictionary to a JSON string with proper indentation
    json_data = json.dumps(data, indent=4)    
    # Create a response object with the JSON data and the appropriate media type
    response = Response(content=json_data, media_type="application/json")
    return response

