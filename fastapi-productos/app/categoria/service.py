from typing import List, Optional

from sqlmodel import Session, select

from .model import Categoria
from .schema import CategoriaCreate, CategoriaUpdate


def crear(session: Session, data: CategoriaCreate) -> Categoria:
    categoria = Categoria(**data.model_dump())
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def obtener_todas(
    session: Session, skip: int = 0, limit: int = 10
) -> List[Categoria]:
    statement = select(Categoria).offset(skip).limit(limit)
    return list(session.exec(statement).all())


def obtener_por_id(session: Session, id: int) -> Optional[Categoria]:
    return session.get(Categoria, id)


def actualizar(
    session: Session, id: int, data: CategoriaUpdate
) -> Optional[Categoria]:
    categoria = session.get(Categoria, id)

    if categoria is None:
        return None

    categoria.nombre = data.nombre
    categoria.descripcion = data.descripcion

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def eliminar(session: Session, id: int) -> bool:
    categoria = session.get(Categoria, id)

    if categoria is None:
        return False

    session.delete(categoria)
    session.commit()

    return True
