from typing import List, Dict, Optional

# 🟢 GREEN - Implementación mínima


class StockInsuficienteError(Exception):
    pass


class Producto:
    def __init__(self, nombre: str, precio: float,
                  stock: Optional[int] = None):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def verificar_stock(self, cantidad: int):
        if self.stock is not None and cantidad > self.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente para {self.nombre}")


class DescuentoPorcentaje:
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje
    
    def aplicar(self, monto: float) -> float:
        return monto * (1 - self.porcentaje / 100)


class DescuentoFijo:
    def __init__(self, monto: float):
        self.monto = monto
    
    def aplicar(self, monto: float) -> float:
        return max(0, monto - self.monto)


class CarritoCompras:
    def __init__(self):
        self.items: List[Dict] = []
        self.descuentos = []
    
    def agregar(self, producto: Producto, cantidad: int):
        producto.verificar_stock(cantidad)
        self.items.append({
            'producto': producto,
            'cantidad': cantidad
        })
    
    def total(self) -> float:
        subtotal = sum(item['producto'].precio * item['cantidad'] 
                      for item in self.items)
        
        total_con_descuentos = subtotal
        for descuento in self.descuentos:
            total_con_descuentos = descuento.aplicar(total_con_descuentos)
        
        return total_con_descuentos
    
    def cantidad_items(self) -> int:
        return sum(item['cantidad'] for item in self.items)
    
    def aplicar_descuento(self, descuento):
        self.descuentos.append(descuento)