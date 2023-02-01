class Product:
    def __init__(self, name, category, quantity_in_stock): # По умолчанию первым аргументом во все методы класса подается
        # self - именно так метод получает доступ к экземпляру класса.
        self.name = name
        self.category = category
        self.quantit_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantit_in_stock > 0 else False

eggs = Product('eggs', 'foog', 5)
print(eggs.is_available())