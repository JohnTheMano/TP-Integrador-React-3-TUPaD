from typing import List

from fastapi import APIRouter, HTTPException, Path, Query, status

from app.core.database import SessionDep
from . import service
from .schema import CategoriaCreate, CategoriaRead, CategoriaUpdate


router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.post(
    "/",
    response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED,
)
def crear_categoria(
    categoria: CategoriaCreate,
    session: SessionDep,
):
    return service.crear(session, categoria)


@router.get(
    "/",
    response_model=List[CategoriaRead],
    status_code=status.HTTP_200_OK,
)
def listar_categorias(
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
):
    return service.obtener_todas(session, skip, limit)


@router.get(
    "/{id}",
    response_model=CategoriaRead,
    status_code=status.HTTP_200_OK,
)

def obtener_categoria(
    session: SessionDep,
    id: int = Path(..., gt=0),
):
    categoria = service.obtener_por_id(session, id)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )

    return categoria


@router.put(
    "/{id}",
    response_model=CategoriaRead,
    status_code=status.HTTP_200_OK,
)
def actualizar_categoria(
    id: int,
    categoria: CategoriaUpdate,
    session: SessionDep,
):
    actualizada = service.actualizar(session, id, categoria)

    if actualizada is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )

    return actualizada


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_categoria(
    id: int,
    session: SessionDep,
):
    eliminado = service.eliminar(session, id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )
