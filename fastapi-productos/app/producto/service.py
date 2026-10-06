from typing import List, Optional

from sqlmodel import Session, select

from .model import Producto
from .schema import ProductoCreate, ProductoUpdate


def crear(session: Session, data: ProductoCreate) -> Producto:
    producto = Producto(**data.model_dump())
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def obtener_todos(
    session: Session, skip: int = 0, limit: int = 10
) -> List[Producto]:
    statement = select(Producto).offset(skip).limit(limit)
    return list(session.exec(statement).all())


def obtener_por_id(session: Session, id: int) -> Optional[Producto]:
    return session.get(Producto, id)


def actualizar(
    session: Session, id: int, data: ProductoUpdate
) -> Optional[Producto]:
    producto = session.get(Producto, id)

    if producto is None:
        return None

    producto.nombre = data.nombre
    producto.descripcion = data.descripcion
    producto.precio_base = data.precio_base
    producto.imagen_url = data.imagen_url
    producto.disponible = data.disponible

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto


def eliminar(session: Session, id: int) -> bool:
    producto = session.get(Producto, id)

    if producto is None:
        return False

    session.delete(producto)
    session.commit()

    return True
