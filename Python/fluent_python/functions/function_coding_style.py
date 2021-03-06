"""Python не задумывался как функциональный язык программирования, однако 
имеет в себе некоторые соответсвующие этому стилю инструменты."""

# стандартные математические операции
from operator import mul, add, sub  

# полезные инструменты при работе с функциями
from functools import reduce, partial


print(mul(5, 5), add(5, 5), sub(5, 5), sep='\n')
# 25
# 10
# 0

# аккумулирование результатов и рецедирование последовательность значений 
# к одному
print(reduce(mul, (1, 2, 3, 4)))  
# 24

# Позволяет передать ф-ции n-й аргумент, который будет использован позже при 
# добавлении n+1 аргумента. Для работы с методами использовать метод 
# partialmethod
triple = partial(add, 3)
print(triple(9))
# 12

# Также ф-ции map, all, any и т.п.
