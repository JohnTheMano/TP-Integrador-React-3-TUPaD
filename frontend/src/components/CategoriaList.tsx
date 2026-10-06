import type { Categoria } from '../types/categoria'
import { CategoriaCard } from './CategoriaCard'

type CategoriaListProps = {
    categorias: Categoria[]
    onEdit: (categoria: Categoria) => void
    onDelete: (id: number) => void
}

export const CategoriaList = ({
    categorias,
    onEdit,
    onDelete,
}: CategoriaListProps) => {
    if (categorias.length === 0) {
    return (
        <p className="text-center text-gray-500">
        No hay categorías registradas.
        </p>
    )
    }

    return (
    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {categorias.map((categoria) => (
        <CategoriaCard
            key={categoria.id}
            categoria={categoria}
            onEdit={onEdit}
            onDelete={onDelete}
        />
        ))}
    </div>
    )
}
