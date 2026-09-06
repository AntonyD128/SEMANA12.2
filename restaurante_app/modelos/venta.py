class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        self._usuario_id = valor.strip()

    @property
    def producto_codigo(self) -> str:
        return self._producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        self._producto_codigo = valor.strip()

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError("La cantidad vendida debe ser mayor a cero.")
        self._cantidad = valor

    def __str__(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def convertir_a_diccionario(self) -> dict[str, str | int]:
        """Convierte la venta a un diccionario compatible con JSON."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }