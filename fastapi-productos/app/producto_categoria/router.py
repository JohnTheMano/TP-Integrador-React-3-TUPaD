from fastapi import APIRouter, HTTPException, status

from app.core.database import SessionDep
from . import service
from .schema import ProductoCategoriaCreate, ProductoCategoriaRead


router = APIRouter(
    prefix="/producto-categoria",
    tags=["ProductoCategoria"]
)


@router.post(
    "/",
    response_model=ProductoCategoriaRead,
    status_code=status.HTTP_201_CREATED,
)
def crear_relacion(
    data: ProductoCategoriaCreate,
    session: SessionDep,
):
    return service.crear(session, data)


@router.get(
    "/",
    response_model=list[ProductoCategoriaRead],
)
def listar_relaciones(session: SessionDep):
    return service.obtener_todas(session)


@router.delete(
    "/{producto_id}/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_relacion(
    producto_id: int,
    categoria_id: int,
    session: SessionDep,
):
    eliminado = service.eliminar(session, producto_id, categoria_id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Relación no encontrada",
        )
