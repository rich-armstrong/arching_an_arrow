"""
Sample module to demonstrate list comprehensions and generators.
"""

import random
from pprint import pprint as pp

def list_comp():
    """
    List comprehensions take the following
        * an input sequence
        * a variable representing a member in the sequence
        * an optional filtering predicate
        * an output expression which creates elements in the output list
          from members of the input list that satisfy the predicate

    Comprehension syntax:
        [ exp(x) for x in a_seq if pred(x) ]

    Task: Comment this code.
    Task: Make 3 more list comprehensions

"""

    # comp 1 - create a list of 10 random numbers
    r_num = [ random.randint(-100,100) for x in range(10) ]
    pp(r_num)

    # comp 2 - square those numbers in r_num that are > s0
    r2_num = [ x**2 for x in r_num if x > 0 ]
    pp(r2_num)

    # comp 3-5

def generators():
    """
    List comprehensions are nice but they create entire lists. This could be
    problematic if we needed to create huge sequences. Your computer could
    run out of memory.

    Generators are similar to comprehensions, but instead of creating all of
    the elements at once, it creates and returns just one. You call the
    generator again to get next elements in the list. This is lazy, it's
    generated as required.

    Generator syntax:
        ( expr(x) for x in a_seq if pred(x) )

    The syntax is the same as list comprehensions, but with () instead of [].

    Task: Document the following code.
    Task: Create 3 more generators of your own

    """

    # generator 1 - 100 random ints in the range [-100,100]
    r_num_gen = (random.randint(-100, 100) for x in range(10))
    # print a generator class
    pp(r_num_gen)
    for num in r_num_gen:
        print "num: %s" % (num)

    # generator 2 - square of the positive ints from above
    new_list = [random.randint(-100, 100) for x in range(10)]
    r2_num_gen = (x**2 for x in new_list if x > 0)
    # print a generator class
    pp(r2_num_gen)
    for num in r2_num_gen:
        print "num**2:  %s" % (num)

    # once you exhaust a generator's items, it throws a StopIteration exception.
    # If you need to keep generating things you can create a function that
    # returns a generator,
    def gen_gen(num):
        """
        Generates a generator that returns random numbers
        """
        return (random.randint(-100, 100) for x in range(num))
    for num in gen_gen(10):
        print num
    for num in gen_gen(10):
        print num
    # ... ad infinitum


def main():
    """
    Main driver
    """
    list_comp()
    generators()



if __name__ == '__main__':
    main()
