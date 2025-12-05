from functools import reduce
from operator import *
from itertools import zip_longest

nums = [1, 2, 3]
res = map(lambda x: x * 2, nums)
print(list(res))

nums = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))

nums = [1, 2, 3, 4]
prod = reduce(lambda a, b: a * b, nums)
opProd = reduce(mul, nums)
print(prod)
print(opProd)

cordinates = ["x", "y", "z", "xy", "xz", "yx", "yz", "zx", "zy"]
cordinateValues = [1, 2, 3]
zippedValues = zip(cordinates, cordinateValues)
zippedLongestValues = zip_longest(cordinates, cordinateValues, fillvalue=0)
print(list(zippedValues))
print(list(zippedLongestValues))
