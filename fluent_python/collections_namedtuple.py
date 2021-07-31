from collections import namedtuple


def test_create_namedtuple(*fields):
    """
    namedtuple - это создание класса без методов, но с полями.

    >>> test_create_namedtuple('Intel Core i9', '8 Gb')
    Computer(processor='Intel Core i9', ram='8 Gb')
    """
    Computer = namedtuple('Computer', ['processor', 'ram'])  # Создание класса Computer с полями processor и ram.
    return Computer(*fields)


if __name__ == "__main__":  # launch: python <file_name> -v
    import doctest
    doctest.testmod(name='test_create_namedtuple', verbose=True)
