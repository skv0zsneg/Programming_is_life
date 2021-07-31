from random import choice


def test_choice(subsequence_object):
    """
    choice -- это выбор случайного элемента из последовательности.
    
    >>> res = test_choice([1, 2, 3, 4, 5])
    >>> res in [1, 2, 3, 4, 5]
    True
    """
    return choice(subsequence_object)


if __name__ == "__main__":  # launch: python <file_name> -v
    import doctest
    doctest.testmod(name='test_choice', verbose=True)
