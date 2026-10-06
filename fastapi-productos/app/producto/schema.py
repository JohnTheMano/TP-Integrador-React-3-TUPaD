from pydantic import BaseModel, Field


class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    descripcion: str = Field(..., min_length=1)
    precio_base: float = Field(..., ge=0)
    imagen_url: list[str] = Field(default_factory=list)
    disponible: bool = True


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class ProductoRead(ProductoBase):
    id: int
