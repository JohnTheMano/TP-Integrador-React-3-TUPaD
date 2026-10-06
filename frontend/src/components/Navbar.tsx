export const Navbar = () => {
  return (
    <nav className="border-b border-stone-200 bg-stone-50">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-stone-800 text-sm font-bold text-stone-50">
            C
          </div>

          <div>
            <h1 className="text-lg font-semibold tracking-tight text-stone-900">
              Gestión de Categorías
            </h1>

            <p className="text-xs text-stone-500">
              CRUD de categorías
            </p>
          </div>
        </div>

        <span className="rounded-full border border-stone-200 bg-white px-4 py-2 text-sm font-medium text-stone-600">
          Categorías
        </span>
      </div>
    </nav>
  )
}
