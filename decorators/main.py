import time
import functools


def profile(f):
    """Подсчет времени работы фукции."""
    @functools.wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        res = f(*args, **kwargs)
        elapsed = time.perf_counter() - start
        inner.__n_calls__ += 1
        inner.__total_time__ += elapsed
        return res

    # инициализируем поля для инстанса f
    inner.__n_calls__ = 0
    inner.__total_time__ = 0
    return inner


def memoize(f):
    """Запрет вызова функции с одним и тем же аргументов."""

    cache = {}
    @functools.wraps(f)
    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    inner.__cache__ = cache
    return inner

        

@profile
@memoize
def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(22))
    print(fib.__n_calls__)
    print(fib.__total_time__)
    
 
#  --- OTHER ---
    @classmethod
    def parse(cls, f):
        """Обертка для полного парсинга SOAP ответов с заявками.

        :param f: Ссылка на вызываемую функцию.
        :type f: function
        :return: Возвращается список, в котором содержится словарь или словари, вмещающий в себя все необходимые
        поля заявки или заявок.
        :rtype: list
        """
        @functools.wraps(f)
        def inner(*args, **kwargs):
            raw_response = f(*args, **kwargs)
            bs = BeautifulSoup(raw_response, features="xml")
            claims_list = list()

            def deep(el):
                fields = []
                el_deep = None

                for el_deep in el.find_all(True, recursive=False):
                    fields.append({el_deep.name: deep(el_deep)})
                return el.text if el_deep is None else fields

            for claim in bs.find_all('claim'):
                claim_fields = dict()
                for el in claim.find_all(True, recursive=False):
                    claim_fields.update({el.name: deep(el)})

                claims_list.append(claim_fields)

            return claims_list

        return inner

