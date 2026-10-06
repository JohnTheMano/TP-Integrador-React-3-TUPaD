from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.types import String


class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    precio_base: float
    imagen_url: list[str] = Field(
        default_factory=list,
        sa_column=Column(ARRAY(String))
    )
    disponible: bool = True
