from sqlmodel import Session, select

from .model import ProductoCategoria
from .schema import ProductoCategoriaCreate


def crear(session: Session, data: ProductoCategoriaCreate):
    relacion = ProductoCategoria(**data.model_dump())
    session.add(relacion)
    session.commit()
    session.refresh(relacion)
    return relacion


def obtener_todas(session: Session):
    statement = select(ProductoCategoria)
    return list(session.exec(statement).all())


def eliminar(session: Session, producto_id: int, categoria_id: int):
    relacion = session.get(
        ProductoCategoria,
        (producto_id, categoria_id)
    )

    if relacion is None:
        return False

    session.delete(relacion)
    session.commit()
    return True
