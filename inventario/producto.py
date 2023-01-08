class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        
    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, n_codigo: str) -> None:
        self.__codigo = n_codigo
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n_nombre: str) -> None:
        self.__nombre = n_nombre

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, n_precio: float) -> None:
        self.__precio = n_precio

    def __str__(self) -> str:
        return f'(Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio})'  
    