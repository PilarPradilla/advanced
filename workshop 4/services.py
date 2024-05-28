import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

#Se creo el entorno virtual para instalar las librerias

app = FastAPI()

# Se agrego el middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

##app = FastAPI() --------> no se necesita esto ya que esta repetido

# Conexión a la base de datos
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/public'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

@app.get("/products")
def get_products():
    query = select([products])
    result = session.execute(query)
    products_list = result.fetchall()#------> lista de productos
    session.close()  # Se cierra seccion
    # Formatea la lista de productos como JSON
    products_json = [{"id": product.id, "name": product.name, "description": product.description} for product in products_list]
    return JSONResponse(content=products_json)

@app.post("/products_create") # Se cambio el nombre del servicio web para que no fuera igual al anterior
def create_product(name: str, description: str):
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    session.close()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
