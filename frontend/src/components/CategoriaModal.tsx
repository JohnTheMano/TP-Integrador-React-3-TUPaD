import { useState } from 'react'
import type { Categoria } from '../types/categoria'

type CategoriaModalProps = {
    isOpen: boolean
    categoria: Categoria | null
    onClose: () => void
    onSubmit: (categoria: {
    nombre: string
    descripcion: string
    }) => void
}

export const CategoriaModal = ({
    isOpen,
    categoria,
    onClose,
    onSubmit,
}: CategoriaModalProps) => {
    const [nombre, setNombre] = useState(categoria?.nombre ?? '')
    const [descripcion, setDescripcion] = useState(
    categoria?.descripcion ?? '',
    )
    
    if (!isOpen) {
    return null
    }

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    onSubmit({
        nombre,
        descripcion,
    })
    }

    return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
        <div className="w-full max-w-md rounded-lg bg-white p-6 shadow-xl">
        <h2 className="text-2xl font-bold text-gray-900">
            {categoria ? 'Editar categoría' : 'Nueva categoría'}
        </h2>

        <form onSubmit={handleSubmit} className="mt-6 space-y-4">
            <div>
            <label className="mb-1 block font-medium text-gray-700">
                Nombre
            </label>

            <input
                type="text"
                value={nombre}
                onChange={(event) => setNombre(event.target.value)}
                required
                className="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-blue-500"
            />
            </div>

            <div>
            <label className="mb-1 block font-medium text-gray-700">
                Descripción
            </label>

            <textarea
                value={descripcion}
                onChange={(event) => setDescripcion(event.target.value)}
                required
                className="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-blue-500"
            />
            </div>

            <div className="flex justify-end gap-3">
            <button
                type="button"
                onClick={onClose}
                className="rounded bg-gray-300 px-4 py-2 text-gray-800 hover:bg-gray-400"
            >
                Cancelar
            </button>

            <button
                type="submit"
                className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
            >
                Guardar
            </button>
            </div>
        </form>
        </div>
    </div>
    )
}
