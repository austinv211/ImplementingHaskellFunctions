from typing import List, Any, Callable
from itertools import accumulate, cycle, islice
from functools import reduce
import operator

# zipWith function in python
# zipWith takes a function and 2 lists and zips the list using the operation provided
def myZipWith(f: Callable[[Any, Any], Any], listA: List[Any], listB: List[Any]) -> List[Any]:
    """Return two lists added together
    >>> listA = [1, 2, 3, 4, 5]
    >>> listB = [6, 7, 8, 9, 10]
    >>> myZipWith(operator.add, listA, listB)
    [7, 9, 11, 13, 15]
    """
    return [(f(x[0],x[1])) for x in zip(listA, listB)]
    #alternative
    #return list(map(f, zip(listA, listB)))

# myFoldl function
def myFoldl(f: Callable[[Any, Any], Any], accInit: Any, values: List[Any]) -> Any:
    """foldl using 10 as our initializer and add the numbers in the list
    >>> myFoldl(operator.add, 10, [1, 2, 3, 4, 5])
    25
    """
    return reduce(lambda x, y: f(f(accInit, x), y) if x == values[0] else f(x,y), values)

#addTwo function to show step process in functions
def addTwo(a, b):
    print(a, "+", b, "=", a + b)
    return a + b

# myFoldr function
def myFoldr(f: Callable[[Any, Any], Any], accInit: Any, values: List[Any]) -> Any:
    """foldr using 10 as our initializer and add the numbers in the list
    >>> myFoldr(operator.add, 10, [1, 2, 3, 4, 5])
    25
    """
    if len(values) != 0:
        accInit = f(values[-1], accInit)
        return myFoldr(f, accInit, values[0:-1])
    else:
        return accInit

#perform foldr just by passing a reversed list to myFoldl
def myFoldr2(f: Callable[[Any, Any], Any], accInit: Any, values: List[Any]) -> Any:
    """foldr using 10 as our initializer and add the numbers in the list
    >>> myFoldr(operator.add, 10, [1, 2, 3, 4, 5])
    25
    """
    return myFoldl(f, accInit, values[::-1])

# myCycle function
def myCycle(values: List[Any]) -> List[Any]:
    """Return 5 elements from a cycle of 1, 2, 3
    >>> list(islice(myCycle([1, 2, 3]), 5))
    [1, 2, 3, 1, 2]
    """
    return cycle(values)


if __name__ == "__main__":
    # Read player names from the command line
    import doctest
    doctest.testmod(verbose=True)
