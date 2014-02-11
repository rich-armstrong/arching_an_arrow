"""
Used to demo and teach decorators.
"""
from math import sqrt
import time

def log(func_to_log):
    """Logs a function call."""
    def log_wrapper(*args, **kwargs):
        """Wraps a logged function."""
        print "  [LOG] %s (ENTER)" % (func_to_log.__name__)
        result = func_to_log(*args, **kwargs)
        print "  [LOG] %s (EXIT)" % (func_to_log.__name__)
        return result
    return log_wrapper

@log
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
            print "Function[%s] took %s s" % (func_to_time.__name__,
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

def decorators2():
    """More advanced decorators, class-based"""

    class timing_dec:
        """Timing decoration as a class"""
        def __init__(self, f):
            """Init"""
            print "  [LOG2] Inside decorator.__init__"
            self.start_time = time.time()
            self.end_time = 0
            self.func = f
        def __call__(self):
            """Calling"""
            print "  [LOG2] Inside decorator.__call__"
            self.func()
            self.end_time = time.time()
            print "  [LOG2] %s too %ss" % (self.func.__name__,
                self.end_time-self.start_time)

    @timing_dec
    def func_to_time1():
        """Timing 1"""
        print "Howdy, world"
    func_to_time1()

    @timing_dec
    def func_to_time2():
        """Slower function to time"""
        s = 0.0
        for x in range(1000000):
            s += sqrt(x)
        print "Val= %.4f" % s
    func_to_time2()


def main():
    """Main driver"""
    decorators1()
    decorators2()



if __name__ == '__main__':
    main()