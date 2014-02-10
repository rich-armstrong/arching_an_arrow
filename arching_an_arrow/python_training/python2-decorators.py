"""
Used to demo and teach decorators.
"""
from math import sqrt
import time

def decorators1():
    """
    A decorator is a function that wraps another function. That is,
    a decorator is a function that takes a function and returns a
    function. One does this to add existing functionality to the
    existing function.

    Decorator syntax:
        @decorator_name

    Consider an exmaple. Let's say we have 100 functions in some
    module. We want performant code, so we want to time every function.
    For every function we could do the following:

    def func1():
        start_time = time.time()
        ... do func1's normal stuff
        end_time = time.time()
        print end_time - start_time

    We would have to repeat that code 100 times, once for each function. Since
    DRY is a basic principle of coding, we need a better solution. We can
    create, as I show below, a decorator function that times any given function,
    we just need to add @timeit to each function:

    @timer
    def func1():
        ... do func1's normal stuff ...

    Often, we create a wrapped function that the decorator creates and returns.
    """

    def timer(func_to_time):
        """
        A small function to time other functions; used as decorator.
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func_to_time(*args, **kwargs)
            end_time = time.time()
            print "Function[%s] took %s us" % (func_to_time.__name__,
                end_time-start_time)
            return result
        return wrapper

    @timer
    def slow_func():
        """A slow function."""
        for x in range(500000):
            sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(x)))))))

    @timer
    def fast_func():
        """A faster function."""
        print "Howdy"

    slow_func()
    fast_func()




def main():
    """Main driver"""
    decorators1()



if __name__ == '__main__':
    main()