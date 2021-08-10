from collections import namedtuple
"""
    namedtuple - это создание класса с полями, но без методов.
"""


Computer = namedtuple('Computer', ['processor', 'ram'])  # Создание класса Computer с полями processor и ram.
Computer = namedtuple('Computer', 'processor ram')  # Так тоже можно. 
Computer = namedtuple('Computer', 'processor, ram')  # И так.
my_comp = Computer('intel core i9', '8 gb')

print(my_comp)  # Computer(processor='intel core i9', ram='8 gb')
