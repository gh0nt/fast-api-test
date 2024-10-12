from fastapi import FastAPI
import uvicorn
from app.db.database import  engine, Base
from app import users  # Importar el router de usuarios

app = FastAPI()

#Crear las tablas
def create_tables():
    Base.metadata.create_all(bind=engine) 


# Incluir el router de usuarios
app.include_router(users.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)

