from collections import namedtuple
"""
    namedtuple - это подкласс tuple с возможностью задавать имена полей и имя класса 
    (создание класса с полями, но без методов).
"""


Computer = namedtuple('Computer', ['processor', 'ram'])     # Создание namedtuple Computer с полями processor и ram.
Computer = namedtuple('Computer', 'processor ram')          # Так тоже можно. 
Computer = namedtuple('Computer', 'processor, ram')         # И так.
my_comp = Computer('intel core i9', '8 gb')
print(my_comp)  # Computer(processor='intel core i9', ram='8 gb')

print(my_comp.processor,    # intel core i9
      my_comp[0],           # intel core i9
      my_comp.ram,          # 8 gb
      my_comp[1])           # 8 gb

print(my_comp._fields)  # ('processor', 'ram') - имена полей


data_serv = (['intel core i9', 'intel core i7'], ['8 gb', '8 gb', '8 gb', '8 gb'])  # Итерируемый объект
my_serv = Computer._make(data_serv) # Создание именованного кортежа через _make()
my_serv = Computer(*data_serv)      # Так тоже можно, без использования _make()
print(my_serv)                      # Computer(processor=['intel core i9', 'intel core i7'], ram=['8 gb', '8 gb', '8 gb', '8 gb'])


for k, v in my_serv._asdict().items():  # Итерирование по полям и значениям именованного кортежа. _asdict() возвращает словарь.
    print(f'{k:<9}: {v}')   # processor: ['intel core i9', 'intel core i7']
                            # ram      : ['8 gb', '8 gb', '8 gb', '8 gb']
