import { useEffect, useState } from 'react';
import './catalogo.css';

const CATEGORIAS = [
  'Electricidad',
  'Jardín y exteriores',
  'Herramientas manuales',
  'Ferretería',
  'Madera y construcción',
  'Pintura y acabados',
  'Plomería',
  'Herramientas eléctricas',
  'Almacenamiento y organización',
];

const moneda = new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' });

function Tarjeta({ producto }) {
  return (
    <article className="tarjeta">
      <div className="foto" aria-hidden="true">foto</div>
      <h3>{producto.nombre}</h3>
      <span className="etiqueta">{producto.categoria}</span>
      <div className="pie">
        <span className="precio">{moneda.format(producto.precio)}</span>
        <button type="button" className="agregar">Agregar</button>
      </div>
    </article>
  );
}

export default function Catalogo() {
  const [productos, setProductos] = useState([]);
  const [estado, setEstado] = useState('cargando'); // cargando | listo | error
  const [categoria, setCategoria] = useState('');
  const [busqueda, setBusqueda] = useState('');

  useEffect(() => {
    let cancelado = false;
    setEstado('cargando');
    const url = categoria ? `/products?categoria=${encodeURIComponent(categoria)}` : '/products';
    fetch(url)
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error(`HTTP ${respuesta.status}`);
        return respuesta.json();
      })
      .then((datos) => {
        if (!cancelado) {
          setProductos(datos);
          setEstado('listo');
        }
      })
      .catch(() => {
        if (!cancelado) setEstado('error');
      });
    return () => {
      cancelado = true;
    };
  }, [categoria]);

  const visibles = productos.filter((p) => p.nombre.toLowerCase().includes(busqueda.trim().toLowerCase()));

  return (
    <>
      <header className="encabezado">
        <strong>FerreMax</strong>
        <nav aria-label="Principal">
          <a href="#catalogo">Catálogo</a>
          <a href="#ofertas">Ofertas</a>
          <a href="#contacto">Contacto</a>
        </nav>
      </header>
      <main className="contenido" id="catalogo">
        <h1>Catálogo de productos</h1>
        <form className="filtros" onSubmit={(e) => e.preventDefault()}>
          <input
            type="search"
            placeholder="Buscar producto..."
            aria-label="Buscar producto"
            value={busqueda}
            onChange={(e) => setBusqueda(e.target.value)}
          />
          <select aria-label="Categoría" value={categoria} onChange={(e) => setCategoria(e.target.value)}>
            <option value="">Todas las categorías</option>
            {CATEGORIAS.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </form>

        {estado === 'cargando' && <p role="status">Cargando productos...</p>}
        {estado === 'error' && <p role="alert">No pudimos cargar el catálogo. Intenta de nuevo.</p>}
        {estado === 'listo' && visibles.length === 0 && (
          <p className="vacio">No encontramos productos con esos filtros.</p>
        )}
        {estado === 'listo' && visibles.length > 0 && (
          <section className="grid" aria-label="Productos">
            {visibles.map((p) => (
              <Tarjeta key={p.id} producto={p} />
            ))}
          </section>
        )}
      </main>
    </>
  );
}
