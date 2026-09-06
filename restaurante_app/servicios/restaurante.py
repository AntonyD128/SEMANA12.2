from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from .archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self) -> None:
        # Instanciar el servicio de archivos
        self._archivo_servicio = ArchivoServicio()

        # Cargar los datos guardados usando sus métodos correspondientes
        self._productos = self._archivo_servicio.cargar_productos()
        self._usuarios = self._archivo_servicio.cargar_usuarios()
        self._ventas = self._archivo_servicio.cargar_ventas()

    # ------------------ PRODUCTOS ------------------
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto en el Restaurante y actualiza el JSON."""
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        self._archivo_servicio.guardar_datos(self.RUTA_PRODUCTOS, [p.a_diccionario() for p in self._productos])
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_limpio = str(codigo).strip()
        for p in self._productos:
            if str(p.codigo).strip() == codigo_limpio:
                return p
        return None

    def actualizar_prducto(
        self,
        codigo: str,
        nuevo_nombre: str = "",
        nueva_categoria: str = "",
        nuevo_precio: float | None = None,
    ) -> bool:
        """Actualiza un producto y guarda los cambios en el JSON."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        producto.actualizar(
            nombre=nuevo_nombre,
            categoria=nueva_categoria,
            precio=nuevo_precio
        )
        ArchivoServicio.guardar_datos(self.RUTA_PRODUCTOS, [p.a_diccionario() for p in self._productos])
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto y actualiza el archivo JSON."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        self._productos.remove(producto)
        ArchivoServicio.guardar_datos(self.RUTA_PRODUCTOS, [p.a_diccionario() for p in self._productos])
        return True

    def obtener_productos(self) -> list[Producto]:
        return self._productos

    def obtener_categorias_unicas(self) -> set[str]:
        return {prod.categoria for prod in self._productos}

    def existe_categoria(self, categoria: str) -> bool:
        return categoria.strip().lower() in {p.categoria.lower() for p in self._productos}

    # ------------------ USUARIOS ------------------
    def registrar_usuario(self, usuario: Usuario) -> bool:
        self._usuarios.append(usuario)
        ArchivoServicio.guardar_datos(self.RUTA_USUARIOS, [u.a_diccionario() for u in self._usuarios])
        return True

    def obtener_usuarios(self) -> list[Usuario]:
        return self._usuarios

    # ------------------ VENTAS ------------------
    def registrar_producto(self, producto: Producto) -> bool:
        # Verificar si ya existe un producto con el mismo código
        if self.buscar_producto(producto.codigo) is not None:
            return False

        # Agregar el producto a la lista local
        self._productos.append(producto)

        # Guardar la lista actualizada en el archivo JSON
        self._archivo_servicio.guardar_productos(self._productos)

        return True
    def obtener_ventas(self) -> list[Venta]:
        return self._ventas

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def realizar_venta(self, id_usuario: str, codigo_producto: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(id_usuario)
        producto = self.buscar_producto(codigo_producto)

        # 1. Validar que el usuario y el producto existan
        if usuario is None or producto is None:
            return False

        # 2. Validar que exista suficiente stock disponible
        if producto.stock < cantidad:
            return False

        # 3. Restar la cantidad vendida al stock
        producto.stock -= cantidad

        # 4. Registrar la nueva venta
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)

        # 5. Guardar los datos actualizados en los archivos JSON
        self._archivo_servicio.guardar_productos(self._productos)
        self._archivo_servicio.guardar_ventas(self._ventas)

        return True
    def obtener_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    
    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float, nuevo_stock: int) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock

        # Guardar los cambios actualizados en el JSON
        ArchivoServicio.guardar_datos(self.RUTA_PRODUCTOS, [p.a_diccionario() for p in self._productos])
        return True