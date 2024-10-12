from app.db import models
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import schemas
from app.db.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.get("/")
def obtener_usuarios(db: AsyncSession = Depends(get_db)):
    # Cambiar el retorno para obtener los usuarios desde la base de datos
    result = db.execute(select(models.User))
    usuarios = result.scalars().all()
    return usuarios

# Endpoint para crear un usuario
@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Endpoint para obtener todos los usuarios
@router.get("/users/", response_model=list[schemas.User])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users
