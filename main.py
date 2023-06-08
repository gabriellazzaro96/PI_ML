from fastapi import FastAPI
from pydantic import BaseModel  #Esta clase garantiza que los tipos de datos que se almacenen en la clase, sean iguales a los definidos
from typing import Optional     #Esta clase permite que el ingreso de un atributo sea opcional
import pandas as pd
from enum import Enum
import numpy as np

app = FastAPI()

df = pd.read_csv("movies_clean.csv")

def cantidad_filmaciones_mes(mes):
    cantidad = 0
    for pelicula in df.values():
        if df["release_month"] == mes:
            cantidad += 1
    return cantidad

@app.get("/cantidad-filmaciones_mes/{mes}")
def get_cantidad_filmaciones_mes(mes: int):
    df1 = df[df['release_month'] == mes]
    cantidad = df1.shape[0]
    return cantidad

@app.get("/cantidad-filmaciones_dia/{dia}")
def get_cantidad_filmaciones_dia(dia: int):
    df1 = df[df['release_day'] == dia]
    cantidad = df1.shape[0]
    return cantidad

@app.get("/score_titulo/{title}")
def get_score_titulo(title: str):
    df1 = df[df['title'].notna() & (df['title'] == title)]
    response = df1[['title', 'release_year', 'popularity']].to_dict(orient='records')
    return response

@app.get("/votos_titulo/{title}")
def votos_titulo(title: str ):
    df1 = df[(df['title'].notna()) & (df['title'] == title) & (df['vote_count'] >= 2000)]
    if df1.empty:
        return {'mensaje' : 'No posee la cantidad de votos minimos'}
    else:
        resp = df1[['title','vote_count','vote_average']].to_dict(orient='records')
        return resp         
        
@app.get("/actor/{actor}")
def get_actor_exito(actor: str):
    df1 = df[df['cast'].notna() & df['cast'].str.contains(actor)]
    participaciones = df1.shape[0]
    retorno = df1['return'].sum()
    prom_retorno = retorno/participaciones
    #resp = [actor,retorno,participaciones,prom_retorno]
    resp = {
        'actor': actor,
        'exito': retorno,
        'participaciones': participaciones,
        'promedio del retorno':prom_retorno
    }
    return resp


# Se ingresa el nombre de un director que se encuentre 
# dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
# Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno 
# individual, costo y ganancia de la misma.

@app.get("/director/{director}")
def get_director(director: str):
    df1 = df[df['director'].notna() & df['director'].str.contains(director)]
    retorno_dir = df1['return'].sum() 
    resp = df1[['title', 'release_date', 'return', 'budget', 'earns']].to_dict(orient='records')
    
    return [director, retorno_dir, resp]
   


