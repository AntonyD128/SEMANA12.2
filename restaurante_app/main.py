from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.restaurante import Restaurante 
from servicios.archivo_servicio import ArchivoServicio

OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar productos"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar Usuarios"),
    ("8", "Eliminar usuario"),
    ("9", "Mostrar categorias unicas"),
    ("10", "Realizar Venta"),
    ("11", "Consultar ventas de usuario"),
    ("12", "Salir del programa"),
)

def pedir_texto(mensaje:str)-> str:
    return input(mensaje).strip()

def mostrar_menu()-> None:
    print("\n--- MENU PRINCIPAL ---")
    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")
def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = pedir_texto("Código: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría: ")
    precio = float(pedir_texto("Precio: "))
    stock = int(pedir_texto("Stock inicial: "))

    nuevo_p = Producto(
        codigo=codigo,
        nombre=nombre,
        categoria=categoria,
        precio=precio,
        stock=stock
    )
    
    if restaurante.registrar_producto(nuevo_p):
        print("Producto registrado correctamente.")
    else:
        print("Error: Ya existe un producto con ese código.")

def buscar_producto(restaurante:Restaurante) -> None:
    print("\n---BUSCAR PRODUCTO ---")
    codigo = pedir_texto("Codigo del producto: ")
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(f"Producto encontrado: {producto.nombre}")

def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar producto ---")
    codigo = pedir_texto("Código del producto: ")

    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return

    print("Deje un campo vacío si no desea modificarlo.")
    nuevo_nombre = pedir_texto("Nuevo nombre: ")
    nueva_categoria = pedir_texto("Nueva categoría: ")
    nuevo_precio_texto = pedir_texto("Nuevo precio: ")

    try:
        nuevo_precio = float(nuevo_precio_texto) if nuevo_precio_texto else None
        actualizado = restaurante.actualizar_producto(
            codigo,
            nuevo_nombre,
            nueva_categoria,
            nuevo_precio,
        )

        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")
    except ValueError as error:
        print(error)
def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar producto ---")
    id_producto = pedir_texto("Ingrese el ID del producto a eliminar: ")
    
    if restaurante.eliminar_producto(id_producto):
        print("Producto eliminado correctamente.")
    else:
        print("No se encontró ningún producto con ese ID.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")
    if not restaurante._productos:
        print("No hay productos registrados.")
    else:
        for p in restaurante._productos:
            print(p)  # Esto llamará automáticamente al método __str__ de Producto


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")
    
    # 1. Solicitar todos los datos del usuario
    identificacion = pedir_texto("Ingrese la ID: ")
    nombre = pedir_texto("Ingrese el nombre del usuario: ")
    correo = pedir_texto("Ingrese el correo del usuario: ")
    celular = pedir_texto("Ingrese el celular del usuario (opcional): ")
 

    try:
        # 2. Instanciar el objeto Usuario
        usuario = Usuario(identificacion, nombre,correo, celular)

        # 3. Enviar el objeto usuario completo a la función
        if restaurante.registrar_usuario(usuario):
            print("Usuario registrado exitosamente.")
        else:
            print("No se pudo registrar el usuario.")
            
    except ValueError as e:
        print(f"Error de validación: {e}")

def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de usuarios ---")
    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for indice, usuario in enumerate(usuarios):
        print(f"{indice + 1}. {usuario}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías únicas ---")
    categorias = restaurante.obtener_categorias_unicas()

    if len(categorias) == 0:
        print("No hay categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")

    categoria_consultada = pedir_texto("\nConsultar si existe una categoría (Enter para omitir): ")
    if categoria_consultada:
        if restaurante.existe_categoria(categoria_consultada):
            print("La categoría existe en el restaurante.")
        else:
            print("La categoría no existe en el restaurante.")
def realizar_venta(restaurante: Restaurante)-> None:
    print("\n--- REALIZAR VENTA ---")
    id_usuario = pedir_texto("Ingrese ID del usuario: ")
    codigo_prod = pedir_texto("Ingrese código del producto: ")
    cant_texto = pedir_texto("Ingrese cantidad: ")
    try:
        cantidad = int(cant_texto)
        if restaurante.realizar_venta(id_usuario, codigo_prod, cantidad):
            print("¡Venta realizada con éxito!")
        else:
            print("Error: No se pudo realizar la venta. Verifique datos o stock disponible.")
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")

def consultar_venta_usuario(restaurante: Restaurante) -> None:
    print("\n---CONSULTAR VENTAS DEL USUARIO---")
    id_usuario = pedir_texto("Ingrese ID del usuario: ")
    ventas = restaurante.obtener_ventas_por_usuario(id_usuario)
    if not ventas:
        print("El usuario no registra ventas.")
    else:
        for v in ventas:
            print(f"Producto: {v.producto_codigo} | Cantidad: {v.cantidad}")
def eliminar_usuario(restaurante: Restaurante) -> None:
    print("\n--- ELIMINAR USUARIO ---")
    id_usuario = pedir_texto("Ingrese ID del usuario a eliminar: ")
    exito = restaurante.eliminar_usuario(id_usuario)
    if exito:
        print("Usuario eliminado correctamente.")
    else:
        print("Error: No se encontró ningún usuario con ese ID.")



def main() -> None:
    restaurante = Restaurante()

    acciones = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante),
        "4": lambda: eliminar_producto(restaurante),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: eliminar_usuario(restaurante),
        "9": lambda: mostrar_categorias(restaurante),
        "10": lambda: realizar_venta(restaurante),
        "11": lambda: consultar_venta_usuario(restaurante),
    }

    while True:
        mostrar_menu()
        opcion = pedir_texto("Seleccione una opción: ")

        if opcion == "12":
            print("Gracias por utilizar el sistema de restaurante.")
            break

        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
        else:
            accion()

def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = pedir_texto("Ingrese el código del producto a actualizar: ")
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Error: No se encontró un producto con ese código.")
        return

    print(f"Producto encontrado: {producto}")
    nombre = pedir_texto(f"Nuevo nombre [{producto.nombre}]: ") or producto.nombre
    categoria = pedir_texto(f"Nueva categoría [{producto.categoria}]: ") or producto.categoria

    try:
        precio_input = pedir_texto(f"Nuevo precio [{producto.precio}]: ")
        precio = float(precio_input) if precio_input else producto.precio

        stock_input = pedir_texto(f"Nuevo stock [{producto.stock}]: ")
        stock = int(stock_input) if stock_input else producto.stock

        exito = restaurante.actualizar_producto(codigo, nombre, categoria, precio, stock)
        if exito:
            print("Producto actualizado correctamente.")
        else:
            print("Error al actualizar el producto.")
    except ValueError:
        print("Error: El precio y el stock deben ser números válidos.")


if __name__ == "__main__":
    main()
