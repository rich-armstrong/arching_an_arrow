"""
Python3-Context Managers

A context manager is a class that contains the
  __enter__
  __exit__
methods that are used in tandem with the 'with' keyword. This allows you to
use a class to place boundaries around code blocks. For example, by using the
'with' keyword we can turn code we intend to do the folllowing,
  ...do stuff
  init()
  ... do more stuff...
  cleanup()

For example, if we wanted to time a code block we could try something like,
  start_time = time.time()
    code to time here
  end_time = time.time()
  print "Duration is %s" % (end_time-start_time)
This example shows how to implement this.

"""
import contextlib
import math
import time

from contextlib import contextmanager

def cm1():
    """Context manager example: timing a code block."""

    class TimingMgr:
        """A simple CM to time code"""
        def __init__(self, label):
            """Constructor"""
            self.label = label
            self.start = None

        def __enter__(self):
            """Called after the 'with' stmt and starts timing."""
            self.start = time.time()

        def __exit__(self, exc_ty, exc_val, exc_tb):
            """Called when exiting the block."""
            end = time.time()
            print "{}: {}s".format(self.label, end - self.start)

    # now, let's time some code
    with TimingMgr("Timing a million sqrts"):
        for x in range(1000000):
            math.sqrt(x)

def cm2():
    """We can use the class-based technique to create a context manager. Or, we
    can use another Python-supported technique. It has two parts.

    (FIRST PART)
    is to use the @contextlib decorator from the contextlib module.

    (SEOND PART)
    create a function that has the following structure:
    def cm_func(args,kwrgs):
        exprs1
        try:
            exprs2
            yield
        finally:
            exprs3

    The following example shows us how to do this.
    """

    @contextmanager
    def TimingMgrFunc(label):
        """Used as a contextmanager"""
        start_time = time.time()
        try:
            yield
        finally:
            end_time = time.time()
            print "{}: {}s".format(label, end_time-start_time)

    with TimingMgrFunc("A million sqrts"):
        for x in range(1000000):
            math.sqrt(x)

def main():
    cm1()
    cm2()

if __name__ == '__main__':
    main()