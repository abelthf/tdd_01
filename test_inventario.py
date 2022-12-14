import pytest

from inventario import Inventario, InvalidQuantityException, NoSpaceException

def test_compra_y_venta_nikes_adidas():
    # Creacion de objeto inventario
    inventario = Inventario()
    assert inventario.limite == 100
    assert inventario.total_items == 0

    # Aniade las nuevas zapatillas Nike
    inventario.add_nuevo_stock('Zapatillas Nike', 50.00, 10)
    assert inventario.total_items == 10

    # Agrega los nuevos pantalones de chandal Adidas
    inventario.add_nuevo_stock('Pantalones Adidas', 70.00, 5)
    assert inventario.total_items == 15

    # Retire 2 zapatillas para vender al primer cliente
    inventario.remove_stock('Zapatillas Nike', 2)
    assert inventario.total_items == 13

    # Retire 1 pantalon de chandal para venderlo al proximo cliente
    inventario.remove_stock('Pantalones Adidas', 1)
    assert inventario.total_items == 12


def test_inventario_default():
    """Test que tiene por defecto el limite =100"""
    inventario = Inventario()
    assert inventario.limite == 100
    assert inventario.total_items == 0


def test_limite_inventario_personalizado():
    """Test que tiene un limite personalizado"""
    inventario = Inventario(limite=25)
    assert inventario.limite == 25
    assert inventario.total_items == 0

@pytest.fixture
def no_stock_inventario():
    """Retorna un inventario vacio que puede almacenar 10 items"""
    return Inventario(10)


def test_add_nuevo_stock_satisfactorio(no_stock_inventario):
    no_stock_inventario.add_nuevo_stock('Test Casaca', 10.00, 5)
    assert no_stock_inventario.total_items == 5
    assert no_stock_inventario.stocks['Test Casaca']['precio'] == 10.00
    assert no_stock_inventario.stocks['Test Casaca']['cantidad'] == 5


# @pytest.mark.parametrize('nombre,precio,cantidad,exception', [
#     ('Test Casaca', 10.00, 0, InvalidQuantityException(
#         'No se puede agregar una cantidad de 0. Todo stock nuevo debe tener al menos 1 item'))])
# def test_add_new_stock_bad_input(nombre, precio, cantidad, exception):
#     inventario = Inventario(10)
#     try:
#         inventario.add_nuevo_stock(nombre, precio, cantidad)
#     except InvalidQuantityException as inst:
#         # Primero asegurese de que la excepcion sea del tipo correcto
#         assert isinstance(inst, type(exception))
#         # Asegurarse de que las excepciones tengan el mismo mensaje
#         assert inst.args == exception.args
#     else:
#         pytest.fail("Error esperado pero no encontrado")


@pytest.mark.parametrize('nombre,precio,cantidad,exception', [
    ('Test Casaca', 10.00, 0, InvalidQuantityException(
        'No se puede agregar una cantidad de 0. Todo stock nuevo debe tener al menos 1 item')),
    ('Test Casaca', 10.00, 25, NoSpaceException(
        'No se pueden agregar estos 25 items. Solo se pueden almacenar 10 items mas'))
])
def test_add_new_stock_bad_input(nombre, precio, cantidad, exception):
    inventario = Inventario(10)
    try:
        inventario.add_nuevo_stock(nombre, precio, cantidad)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # Primero asegurese de que la excepcion sea del tipo correcto
        assert isinstance(inst, type(exception))
        # Asegurarse de que las excepciones tengan el mismo mensaje
        assert inst.args == exception.args
    else:
        pytest.fail("Error esperado pero no encontrado")
