import pytest
from shoping_store import CarritoCompras, DescuentoFijo, DescuentoPorcentaje, Producto, StockInsuficienteError

# 🔴 RED - Tests que fallan inicialmente

class TestPosrcentaje:
    
    def test_aplicar_descuento_porcentaje(self):
        descuento = DescuentoPorcentaje(15)  # 15% de descuento
        monto_inicial = 200.0
        monto_final = descuento.aplicar(monto_inicial)
        assert monto_final == 170.0  # 200 - 30 (15% de 200)
    
    def test_aplicar_descuento_fijo(self):
        descuento = DescuentoFijo(30)  # $30 de descuento
        monto_inicial = 100.0
        monto_final = descuento.aplicar(monto_inicial)
        assert monto_final == 70.0  # 100 - 30
    
    def test_aplicar_descuento_fijo_no_negativo(self):
        descuento = DescuentoFijo(150)  # $150 de descuento
        monto_inicial = 100.0
        monto_final = descuento.aplicar(monto_inicial)
        assert monto_final == 0.0  # No puede ser negativo
class TestShopingCar:
    
    def test_carrito_vacio_inicialmente(self):
        carrito = CarritoCompras()
        assert carrito.total() == 0
        assert carrito.cantidad_items() == 0
    
    def test_agregar_producto_simple(self):
        carrito = CarritoCompras()
        producto = Producto("laptop", 1000.0)
        carrito.agregar(producto, cantidad=2)
        assert carrito.total() == 2000.0
        assert carrito.cantidad_items() == 2
    
    def test_aplicar_descuento_porcentaje(self):
        carrito = CarritoCompras()
        producto = Producto("mouse", 50.0)
        carrito.agregar(producto, cantidad=4)
        carrito.aplicar_descuento(DescuentoPorcentaje(20))  # 20% descuento
        assert carrito.total() == 160.0  # 200 - 40
    
    def test_aplicar_multiple_descuentos(self):
        carrito = CarritoCompras()
        producto = Producto("teclado", 100.0)
        carrito.agregar(producto, cantidad=5)
        carrito.aplicar_descuento(DescuentoPorcentaje(10))
        carrito.aplicar_descuento(DescuentoFijo(50))
        # 500 -> 450 (10%) -> 400 (50 fijo)
        assert carrito.total() == 400.0
    
    def test_stock_insuficiente_lanza_excepcion(self):
        producto = Producto("webcam", 200.0, stock=3)
        carrito = CarritoCompras()
        with pytest.raises(StockInsuficienteError):
            carrito.agregar(producto, cantidad=5)