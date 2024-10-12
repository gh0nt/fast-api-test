from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/fast_api_test"

# Crear el motor de base de datos asíncrono
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear una sesión asíncrona para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)

# Definir la base para los modelos
Base = declarative_base()

# Función para obtener una sesión de la base de datos
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
