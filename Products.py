class ProductFactory:
    def __init__(self):
        self._productfactory = [Products('Хлеб', 10), Products('Гречка', 15), Products('Пиво', 50)]
        self._fruitfactory = [Fruits('Яблоки', 50), Fruits('Бананы', 25), Fruits('Киви', 30)]
        self.products_list = []
        self.fruit_list = []
        self.fruit_cost = []
        self.products_cost = []
        for i in range(len(self.products)):
            self.products_list.append(self.products[i].getName() + f' {self.products[i].getCost()} руб')
            self.products_cost.append(self.products[i].getCost())
        for i in range(len(self.fruit)):
            self.fruit_list.append(self.fruit[i].getName() + f' {self.products[i].getCost()} руб за кг')
            self.fruit_cost.append(self.products[i].getCost())
    @property
    def products(self):
        return self._productfactory
    @property
    def fruit(self):
        return self._fruitfactory

class Products:
    def __init__(self, name, cost:int):
        self.cost = cost
        self.name = name

    def getCost(self):
        return self.cost

    def getName(self):
        return self.name

class Fruits(Products):
    def __init__(self, name, cost_kg):
        self.cost_kg = cost_kg
        self.name = name

