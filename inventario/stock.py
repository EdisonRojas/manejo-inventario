from inventario.producto import Producto

class Stock:
    
    def __init__(self) -> None:
        self.__productos: list[Producto] = []

    def comprobar_producto(self, codigo: str) -> bool:
        return any(prod.codigo == codigo for prod in self.__productos)

    def agregar_producto(self, producto: Producto) -> None:
        if self.comprobar_producto(producto.codigo):
            raise ValueError(f"El producto: {producto.codigo} ya existe.")
        else:        
            self.__productos.append(producto)
    
    def quitar_producto(self, producto: Producto) -> None:
        self.__productos.remove(producto)            
    
    @property
    def productos(self) -> list[Producto]:
        return self.__productos
  