# Importacion de librerias necesarias
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# app = FastAPI() instancia para poder definir y gestionar rutas y endpoints de la API 
app = FastAPI()

#validacion de datos pydanti libreria...
#...garantizan la entrada de los datos...
#para permitir que la entrada sea opcional from typing import Optional 
class Book(BaseModel):
    titulo: str
    autor: str
    paginas: int
    genero: Optional[str]

#ruta GET pathroot (raiz)
# decorador = @ registra la funcion 
@app.get("/")
def index():
    return {"Hi": "I'm Daniel :) "}

#ruta libros
@app.get("/books/{id}")
def show_book(id:int):
    return {"Book number": id}

# ruta POST que es usada por:
# Clase Book(BaseModel):
# ...  
@app.post("/books")
def create_book(book: Book):
    return {"message": f"Inserted {book.titulo} book"}