from inventario.stock import Stock
from inventario.producto import Producto
from inventario.excel_exporter import ExcelExporter

def ejecutar() -> None:
    stock = Stock()
    
    prod1 = Producto("p1", "Laptop Lenovo Thinkpad T256", 1500)
    stock.agregar_producto(prod1)
    
    prod2 = Producto("p2", "Celular Xiaomi Redmi Note 10", 400)
    stock.agregar_producto(prod2)
    
    prod3 = Producto("p3", "Mouse Inalambrico Logitech M190", 25)
    stock.agregar_producto(prod3)
    
        
    prod4 = Producto("p4", "Camisa Tommy", 50)
    stock.agregar_producto(prod4)
    
    prod5 = Producto("p5", "Calculadora cientifica Casio", 45.99)
    stock.agregar_producto(prod5)
    
    stock.quitar_producto(prod1)

    exporter = ExcelExporter()
    exporter.exportar(stock, "D:\\stock_productos.xlsx")
    
if __name__ == "__main__":
    ejecutar()