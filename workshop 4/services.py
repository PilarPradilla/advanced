import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

engine = create_engine('postgresql://postgres:postgres@localhost:55762/public')
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

##app = FastAPI() --------> no se necesita esto ya que esta repetido

@app.get("/products")
def get_products():
    query = select([products])
    result = session.execute(query)
    products_list = result.fetchall() #------> lista de productos
    session.close()  # Se cierra seccion
    return JSONResponse(content=[{"id": product.id, "name": product.name, "description": product.description} for product in products_list]) #----> se llena la lista de productos

@app.post("/products_create")
def create_product(name: str, description: str):
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    session.close()  # Close the session after use
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5500)
