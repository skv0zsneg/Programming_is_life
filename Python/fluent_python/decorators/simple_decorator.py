import functools
from re import I
import time


def clock(func):
    # Такое оборачивание не очень хорошо, поскольку не все атрибуты 
    # декорируемый ф-ции копируются (напр., __name__ и __doc__).
    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        
        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - t0
        f_name = func.__name__
        args_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(
            f"{str(k)}={repr(v)}" for k, v in kwargs.items())
        all_args = ', '.join((args_str, kwargs_str))

        print('[%0.8fs] %s(%s) -> %r' % (elapsed, f_name, all_args, result))
        
        return result
    return inner


def clock_2(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        
        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - t0
        f_name = func.__name__
        args_list = []
        if args:
            args_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            args_list.append(', '.join(
                f"{str(k)}={repr(v)}" for k, v in kwargs.items()))

        print('[%0.8fs] %s(%s) -> %r' % (elapsed, f_name, 
                                         ', '.join(args_list), result))
        
        return result
    return inner

def clock_3(verbose=True):
    def decorate(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            t0 = time.perf_counter()
            
            result = func(*args, **kwargs)

            elapsed = time.perf_counter() - t0
            f_name = func.__name__
            args_list = []
            if args:
                args_list.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                args_list.append(', '.join(
                    f"{str(k)}={repr(v)}" for k, v in kwargs.items()))
            if verbose:
                print('[%0.8fs] %s(%s) -> %r' % (elapsed, f_name, 
                                                ', '.join(args_list), result))
            
            return result
        return inner
    return decorate


@clock
def sum(a: int, b: int, pow_two: bool = False) -> int:
    return a + b if not pow_two else (a + b) ** 2

@clock_2
def sum_2(a: int, b: int, pow_two: bool = False) -> int:
    return a + b if not pow_two else (a + b) ** 2

@clock_3(verbose=False)
def sum_3(a: int, b: int, pow_two: bool = False) -> int:
    return a + b if not pow_two else (a + b) ** 2


def main():
    sum(4, 4)
    sum(2, 2, pow_two=True)

    sum_2(4, 4)
    sum_2(2, 2, pow_two=True)
    
    sum_3(4, 4)
    sum_3(2, 2, pow_two=True)

    # [0.00000132s] sum(4, 4, ) -> 8
    # [0.00000280s] sum(2, 2, pow_two=True) -> 16
    # [0.00000090s] sum_2(4, 4) -> 8
    # [0.00000174s] sum_2(2, 2, pow_two=True) -> 16


if __name__ == "__main__":
    main()
