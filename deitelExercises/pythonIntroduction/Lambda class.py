# lambda - you can assign them into a variable, pass into another function.
add = lambda x, y: x + y
sub = lambda x, y: x - y
print(add.__name__)
print(sub.__name__)


# =============================================================================================
def add(a, b):
    return a + b


def sub(c, d):
    return d - c


def mul(e, f):
    return e * f


def operate(x, y, fn):  # higher order function
    return fn(x, y)


val_sub = operate(5, 12, sub)
val_add = operate(5, 12, add)
val_mul = operate(5, 12, mul)

print(val_add)
print(val_sub)
print(val_mul)


# ===========================================================================
def operate(x, y, func):
    return func(x, y)


div = operate(6, 42, lambda x, y: y / x)
add = operate(15, 12, lambda x, y: x + y)
mul = operate(9, 2, lambda x, y: x * y)
print(div)
print(add)
print(mul)


# ================================================================================================
def multiple(x, func):
    return func(x)


square = multiple(5, lambda x: x ** 2)
print(square)

cube = multiple(6, lambda x: x ** 3)
print(cube)

# import builtins, dir builtins, import antigravity(Takes you to a page)
# =========================================================================================================
print(any([True, False, True]))

names = ["Amaka", "Segun", "comb", "Samson", "foil"]

print(all(name.istitle() for name in names))

peoples = [{"name": "omosetan Omorele", "age": 30, "year_of_exp": 4, "language": ["Python", "Java"]},
           {"name": "John Doe", "age": 25, "year_of_exp": 2, "language": ["JavaScript", "C#"]},
           {"name": "Amaka Stephen", "age": 19, "year_of_exp": 3, "language": ["Python"]}]

print([people["age"] <= 28 and "Python" in people["language"] for people in peoples])
print([people["name"] for people in peoples if people["age"] <= 28 and "Python" in people["language"]])
# ==========================================================================================================
# map
# A map will give map object. I need "list" keyword to make it readable
# map object evaluates only once.

map_object = map(lambda x: x ** 2, range(1, 10))
list_ = list(map_object)
print(list_)

map_object2 = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
listt_ = list(map_object2)
print(listt_)


# ==================================================================================================
# FILTER
def is_even(x):
    return x % 2 == 0


filter_obj = list(filter(is_even, range(1, 10)))
print(filter_obj)
# ========================================================================================================
from functools import reduce

add = reduce(lambda x, y: x + y, range(1, 11))
print(add)

fruits = ["Apple", "Pear", "Pineapple", "Orange", "Watermelon", "Banana", "Cucumber"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
print(longest)
print(max(fruits, key=len))
print(sorted(fruits, key=lambda x: x[-1]))  # key = lambda x:x[len(x)-1]
