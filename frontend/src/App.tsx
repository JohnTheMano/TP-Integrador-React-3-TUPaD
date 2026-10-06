import { useEffect, useState } from 'react'
import { Navbar } from './components/Navbar'
import { CategoriaList } from './components/CategoriaList'
import { CategoriaModal } from './components/CategoriaModal'
import type { Categoria } from './types/categoria'

const API_URL = 'http://127.0.0.1:8000'

export const App = () => {
  const [categorias, setCategorias] = useState<Categoria[]>([])
  const [modalAbierto, setModalAbierto] = useState(false)
  const [categoriaSeleccionada, setCategoriaSeleccionada] =
    useState<Categoria | null>(null)

  useEffect(() => {
    const cargarCategorias = async () => {
      try {
        const response = await fetch(`${API_URL}/categorias/`)

        if (!response.ok) {
          throw new Error('Error al obtener las categorías')
        }

        const data: Categoria[] = await response.json()
        setCategorias(data)
      } catch (error) {
        console.error('Error:', error)
      }
    }

    cargarCategorias()
  }, [])

  const handleCreate = async (datos: {
    nombre: string
    descripcion: string
  }) => {
    try {
      const response = await fetch(`${API_URL}/categorias/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(datos),
      })

      if (!response.ok) {
        throw new Error('Error al crear la categoría')
      }

      const nuevaCategoria: Categoria = await response.json()

      setCategorias((prev) => [...prev, nuevaCategoria])
      setModalAbierto(false)
    } catch (error) {
      console.error('Error:', error)
    }
  }

  const handleUpdate = async (datos: {
    nombre: string
    descripcion: string
  }) => {
    if (!categoriaSeleccionada) {
      return
    }

    try {
      const response = await fetch(
        `${API_URL}/categorias/${categoriaSeleccionada.id}`,
        {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(datos),
        },
      )

      if (!response.ok) {
        throw new Error('Error al actualizar la categoría')
      }

      const categoriaActualizada: Categoria = await response.json()

      setCategorias((prev) =>
        prev.map((categoria) =>
          categoria.id === categoriaActualizada.id
            ? categoriaActualizada
            : categoria,
        ),
      )

      setModalAbierto(false)
      setCategoriaSeleccionada(null)
    } catch (error) {
      console.error('Error:', error)
    }
  }

  const handleDelete = async (id: number) => {
    try {
      const response = await fetch(`${API_URL}/categorias/${id}`, {
        method: 'DELETE',
      })

      if (!response.ok) {
        throw new Error('Error al eliminar la categoría')
      }

      setCategorias((prev) =>
        prev.filter((categoria) => categoria.id !== id),
      )
    } catch (error) {
      console.error('Error:', error)
    }
  }

  const abrirModalCrear = () => {
    setCategoriaSeleccionada(null)
    setModalAbierto(true)
  }

  const abrirModalEditar = (categoria: Categoria) => {
    setCategoriaSeleccionada(categoria)
    setModalAbierto(true)
  }

  const cerrarModal = () => {
    setModalAbierto(false)
    setCategoriaSeleccionada(null)
  }

  const handleSubmit = async (datos: {
    nombre: string
    descripcion: string
  }) => {
    if (categoriaSeleccionada) {
      await handleUpdate(datos)
    } else {
      await handleCreate(datos)
    }
  }

  return (
    <div className="flex min-h-screen flex-col bg-gray-100">
      <Navbar />

      <main className="mx-auto w-full max-w-6xl flex-1 px-6 py-10">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <h2 className="text-4xl font-extrabold text-gray-900">
              Categorías
            </h2>

            <p className="mt-2 text-lg text-gray-600">
              Administración de categorías de productos
            </p>
          </div>

          <button
            onClick={abrirModalCrear}
            className="rounded bg-blue-600 px-5 py-3 font-medium text-white hover:bg-blue-700"
          >
            Nueva categoría
          </button>
        </div>

        <CategoriaList
          categorias={categorias}
          onEdit={abrirModalEditar}
          onDelete={handleDelete}
        />
      </main>

      <CategoriaModal
        isOpen={modalAbierto}
        categoria={categoriaSeleccionada}
        onClose={cerrarModal}
        onSubmit={handleSubmit}
      />
    </div>
  )
}
