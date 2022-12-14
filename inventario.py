class Inventario:
    def __init__(self, limite=100):
        self.limite = limite
        self.total_items = 0
        self.stocks = {}

    # def add_nuevo_stock(self, nombre, precio, cantidad):
    #     self.stocks[nombre] = {
    #         'precio': precio,
    #         'cantidad': cantidad
    #     }
    #     self.total_items += cantidad  

    # def add_nuevo_stock(self, nombre, precio, cantidad):
    #     if cantidad <= 0:
    #         raise InvalidQuantityException(
    #             'No se puede agregar una cantidad de {}. Todo stock nuevo debe tener al menos 1 item'.format(cantidad))
    #     self.stocks[nombre] = {
    #         'precio': precio,
    #         'cantidad': cantidad
    #     }
    #     self.total_items += cantidad

    def add_nuevo_stock(self, nombre, precio, cantidad):
        if cantidad <= 0:
            raise InvalidQuantityException(
                'No se puede agregar una cantidad de {}. Todo stock nuevo debe tener al menos 1 item'.format(cantidad))
        if self.total_items + cantidad > self.limite:
            remaining_space = self.limite - self.total_items
            raise NoSpaceException(
                'No se pueden agregar estos {} items. Solo se pueden almacenar {} items mas'.format(cantidad, remaining_space))
        self.stocks[nombre] = {
            'precio': precio,
            'cantidad': cantidad
        }
        self.total_items += cantidad


class InvalidQuantityException(Exception):
    pass

class NoSpaceException(Exception):
    pass
