import type { Categoria } from '../types/categoria'

type CategoriaCardProps = {
    categoria: Categoria
    onEdit: (categoria: Categoria) => void
    onDelete: (id: number) => void
}

export const CategoriaCard = ({
    categoria,
    onEdit,
    onDelete,
}: CategoriaCardProps) => {
    return (
    <div className="rounded-lg bg-white p-6 shadow-md">
        <p className="text-sm text-gray-500">
        Número: {categoria.id}
        </p>

        <h3 className="mt-1 text-xl font-bold text-gray-900">
        {categoria.nombre}
        </h3>

        <p className="mt-2 text-gray-600">
        {categoria.descripcion}
        </p>

        <div className="mt-4 flex gap-3">
        <button
            onClick={() => onEdit(categoria)}
            className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
        >
            Editar
        </button>

        <button
            onClick={() => onDelete(categoria.id)}
            className="rounded bg-red-600 px-4 py-2 text-white hover:bg-red-700"
        >
            Eliminar
        </button>
        </div>
    </div>
    )
}
