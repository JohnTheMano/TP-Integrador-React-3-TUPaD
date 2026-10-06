import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine




load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("No se encontró DATABASE_URL en el archivo .env")


engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    from app.categoria.model import Categoria
    from app.producto.model import Producto
    from app.producto_categoria.model import ProductoCategoria

    SQLModel.metadata.create_all(engine)



def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
