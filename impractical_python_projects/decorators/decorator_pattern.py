from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass


class DarkRoast(Beverage):

    def cost(self):
        return 20


class CondinentCompliment(Beverage, ABC):

    def __init__(self, beverage):
        self.beverage = beverage


class MochaDecorator(CondinentCompliment):

    def cost(self):
        return self.beverage.cost() + 5


class MochaWithMilkDecorator(CondinentCompliment):

    def cost(self):
        return self.beverage.cost() + 10


dark_roast = DarkRoast()  # This is basic
print(dark_roast.cost())

mocha_decorator = MochaDecorator(dark_roast)  # This is like a top-up on that same object
print(mocha_decorator.cost())

mocha_with_milk_decorator = MochaWithMilkDecorator(mocha_decorator)
print(mocha_with_milk_decorator.cost())  # Decorator on mocha with milk
