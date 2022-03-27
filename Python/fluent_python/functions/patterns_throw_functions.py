"""Паттерн "Стратегия". До применения ф-ций и после.

Суть примера - магазин.
Контекст - корзина покупателя Х с товароми.
Стратегия - выбор скидки для товара.
"""
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import List


# Покупатель
Customer = namedtuple('Customer', 'name shopping_cart') 

# Продукт
Product = namedtuple('Product', 'name price amount')


# Корзина с продуктами
class ShoppingCart:

    def __init__(self, products: List[Product]) -> None:
        self.products = products
    
    def total_price(self) -> float:
        return sum(product.amount * product.price for product in self.products)


    def total_count(self) -> int:
        return sum(product.amount for product in self.products)


# Стратерия
class Promotion(ABC):
    
    @abstractmethod
    def discount(self) -> float:
        """Возвращает скидку."""
        pass


# Контекст
class Order:

    def __init__(self, customer: Customer, 
                 promotion: Promotion = None) -> None:
        self.customer = customer
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = self.customer.shopping_cart.total_price()
        return self.__total
    
    def due(self):
        if self.promotion is None:
            return 0
        return self.total() - self.promotion.discount(self)
        

# Конкретные стратегии
class TenPromotion(Promotion):

    def discount(self, order: Order) -> float:
        """Возвращает скидку 10% если товаров больше 10."""
        if order.shopping_cart.total_count > 10:
            return order.shopping_cart.total_price * 0.1
        return 0

class FivePromotion(Promotion):

    def discount(self, order: Order) -> float:
        """Возвращает скидку 5% если товаров больше 5."""
        if order.shopping_cart.total_count > 5:
            return order.shopping_cart.total_price * 0.05
        return 0


"""
>>> joe = Customer('joe', ShoppingCart(
...     [Product('apple', 10, 5),
...      Product('milk', 10, 5)]
... ))
"""
