# servicios/archivo_servicio.py
# Servicio encargado UNICAMENTE de la persistencia de productos, usuarios
# y ventas en JSON. No conoce reglas de negocio del restaurante
# (duplicados, stock, validez de una venta, etc.): solo sabe leer y
# escribir archivos, y convertir entre objetos y diccionarios.

import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(
        self,
        ruta_productos: str = "restaurante_app/datos/productos.json",
        ruta_usuarios: str = "restaurante_app/datos/usuarios.json",
        ruta_ventas: str = "restaurante_app/datos/ventas.json",
    ) -> None:
        self._ruta_productos = Path(ruta_productos)
        self._ruta_usuarios = Path(ruta_usuarios)
        self._ruta_ventas = Path(ruta_ventas)
    # ------------ Lectura/escritura genérica ------------
    def _leer_lista_json(self, ruta: Path, nombre_archivo: str) -> list:
        """
        Lee un archivo JSON y devuelve su contenido si es una lista. Un
        problema esperado (archivo ausente, JSON inválido, sin permisos,
        contenido que no es una lista) nunca detiene la aplicación: se
        informa y se devuelve una lista vacía.
        """
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"El archivo {nombre_archivo} no tiene un formato JSON válido.")
            return []
        except PermissionError:
            print(f"No hay permisos suficientes para leer {nombre_archivo}.")
            return []

        if not isinstance(datos, list):
            print(f"El archivo {nombre_archivo} debe contener una lista de registros.")
            return []

        return datos

    def _escribir_lista_json(self, ruta: Path, datos: list, nombre_archivo: str) -> bool:
        """Sobrescribe un archivo JSON con la lista de diccionarios recibida."""
        try:
            ruta.parent.mkdir(parents=True, exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"No hay permisos suficientes para guardar {nombre_archivo}.")
            return False

    # ------------ Productos ------------
    def cargar_productos(self) -> list[Producto]:
        registros = self._leer_lista_json(self._ruta_productos, "productos.json")
        productos: list[Producto] = []

        for item in registros:
            if not isinstance(item, dict):
                print("Se encontró un registro de producto con formato inválido y fue omitido.")
                continue
            try:
                producto = Producto(
                    item["codigo"],
                    item["nombre"],
                    item["categoria"],
                    item["precio"],
                    item["stock"],
                )
                productos.append(producto)
            except KeyError as error:
                print(f"Se encontró un registro de producto incompleto (falta {error}) y fue omitido.")
            except ValueError as error:
                print(f"Se encontró un producto con datos inválidos: {error}")

        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        datos = [producto.a_diccionario() for producto in productos]
        return self._escribir_lista_json(self._ruta_productos, datos, "productos.json")

    # ------------ Usuarios ------------
    def cargar_usuarios(self) -> list[Usuario]:
        registros = self._leer_lista_json(self._ruta_usuarios, "usuarios.json")
        usuarios: list[Usuario] = []

        for item in registros:
            if not isinstance(item, dict):
                print("Se encontró un registro de usuario con formato inválido y fue omitido.")
                continue
            try:
                usuario = Usuario(
                    item["identificacion"],
                    item["nombre"],
                    item["correo"],
                    item.get("celular", ""),
                )
                usuarios.append(usuario)
            except KeyError as error:
                print(f"Se encontró un registro de usuario incompleto (falta {error}) y fue omitido.")
            except ValueError as error:
                print(f"Se encontró un usuario con datos inválidos: {error}")

        return usuarios

    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        datos = [usuario.a_diccionario() for usuario in usuarios]
        return self._escribir_lista_json(self._ruta_usuarios, datos, "usuarios.json")

    # ------------ Ventas ------------
    def cargar_ventas(self) -> list[Venta]:
        registros = self._leer_lista_json(self._ruta_ventas, "ventas.json")
        ventas: list[Venta] = []

        for item in registros:
            if not isinstance(item, dict):
                print("Se encontró un registro de venta con formato inválido y fue omitido.")
                continue
            try:
                venta = Venta(
                    item["usuario_id"],
                    item["producto_codigo"],
                    item["cantidad"],
                )
                ventas.append(venta)
            except KeyError as error:
                print(f"Se encontró un registro de venta incompleto (falta {error}) y fue omitido.")
            except ValueError as error:
                print(f"Se encontró una venta con datos inválidos: {error}")

        return ventas

    def guardar_ventas(self, ventas: list[Venta]) -> bool:
        datos = [venta.convertir_a_diccionario() for venta in ventas]
        return self._escribir_lista_json(self._ruta_ventas, datos, "ventas.json")