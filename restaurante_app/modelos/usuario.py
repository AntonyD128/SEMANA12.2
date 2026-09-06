class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str, celular: str = "") -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.celular = celular

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificación no puede estar vacía.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        valor_limpio = (valor or "").strip()
        if not valor_limpio:
            raise ValueError("El correo no puede estar vacío.")
        posicion_arroba = valor_limpio.find("@")
        if posicion_arroba == -1 or "." not in valor_limpio[posicion_arroba + 1:]:
            raise ValueError("El correo debe contener @ y un punto después del @.")
        self._correo = valor_limpio

    @property
    def celular(self) -> str:
        return self._celular

    @celular.setter
    def celular(self, valor: str) -> None:
        self._celular = (valor or "").strip()

    def __str__(self) -> str:
        info = f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"
        if self.celular:
            info += f" | Celular: {self.celular}"
        return info
    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "celular": self.celular
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Usuario':
        return Usuario(
            identificacion=datos.get("identificacion", ""),
            nombre=datos.get("nombre", ""),
            correo=datos.get("correo", ""),
            celular=datos.get("celular", "")
        )