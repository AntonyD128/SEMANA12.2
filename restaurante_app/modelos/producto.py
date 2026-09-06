class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}" 
    @property
    def codigo(self)->str:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo:str)->None:
        if not codigo or not codigo.strip():
            raise ValueError("El codigo del producto no puede estar vacio.")
        self._codigo = codigo

    @property
    def nombre(self)->str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str)->None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = nombre.strip()

    @property
    def categoria(self)->str:
        return self._categoria 

    @categoria.setter
    def categoria(self, categoria:str)-> None:
        if not categoria or not categoria.strip():
            raise ValueError("La categoria del producto no puede estarvacia.")
        self._categoria = categoria.strip()

    @property
    def precio(self)->float:
        return self._precio

    @precio.setter
    def precio(self,precio:float)->None:
        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero.")
        self._precio = precio

    def actualizar(
        self,
        nombre:str="",
        categoria:str="", 
        precio:float|None=None,
    )->None:
        """Actualizar los atributos del producto."""

        if nombre :
            self.nombre = nombre
        if categoria:
            self.categoria = categoria
        if precio is not None:
            self.precio = precio

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
    #SEMANA10 def a_diccionario(self) -> dict:
    def a_diccionario(self) -> dict:  
        return { 
            "codigo": self.codigo,  
            "nombre": self.nombre,  
            "categoria": self.categoria,  
            "precio": self.precio,  
            "stock": self.stock  
        }  

    @classmethod  
    def desde_diccionario(cls, datos: dict):  
        return cls(  
            codigo=datos["codigo"], 
            nombre=datos["nombre"],  
            categoria=datos["categoria"],  
            precio=float(datos["precio"])  
        )  