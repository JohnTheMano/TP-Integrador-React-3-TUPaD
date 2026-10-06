from typing import List

from fastapi import APIRouter, HTTPException, Path, Query, status

from app.core.database import SessionDep
from . import service
from .schema import ProductoCreate, ProductoRead, ProductoUpdate


router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post(
    "/",
    response_model=ProductoRead,
    status_code=status.HTTP_201_CREATED,
)
def crear_producto(
    producto: ProductoCreate,
    session: SessionDep,
):
    return service.crear(session, producto)


@router.get(
    "/",
    response_model=List[ProductoRead],
    status_code=status.HTTP_200_OK,
)
def listar_productos(
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
):
    return service.obtener_todos(session, skip, limit)


@router.get(
    "/{id}",
    response_model=ProductoRead,
    status_code=status.HTTP_200_OK,
)
def obtener_producto(
    session: SessionDep,
    id: int = Path(..., gt=0),
):
    producto = service.obtener_por_id(session, id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return producto


@router.put(
    "/{id}",
    response_model=ProductoRead,
    status_code=status.HTTP_200_OK,
)
def actualizar_producto(
    id: int,
    producto: ProductoUpdate,
    session: SessionDep,
):
    actualizado = service.actualizar(session, id, producto)

    if actualizado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return actualizado


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_producto(
    id: int,
    session: SessionDep,
):
    eliminado = service.eliminar(session, id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )
