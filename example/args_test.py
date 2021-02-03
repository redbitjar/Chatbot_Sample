

# primes = [2,3,5,7,11,13]
# primes2 = [4,6,9]

# def product(*numbers):
#     print(numbers[0])

# product(*primes)

def abc(a,b,c):
    return a,b,c

p = [5,7,9]
print(*p)


def wrapper(*args, **kwargs):
    print('abc')

wrapper()

from functools import wraps

def without_wraps(func):
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper

@without_wraps
def my_func_a():
    """Here is my_func_a doc string text."""
    pass

print( my_func_a.__doc__)
print( my_func_a.__name__)

def with_wraps(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper

@with_wraps
def my_func_b():
    """Here is my_func_a doc string text."""
    pass

print( my_func_b.__doc__)
print( my_func_b.__name__)


def check_input_rules(defaultValue):
    def __decorator(func):
        @wraps(func)
        def __wrapper(*args, **kwargs):
            msg = "#{} argument is negative and will be replaced with defaulted value:{}"
            newArgs = []
            for idx, arg in enumerate(args):
                newArgs.append(arg)
                if isinstance(arg, int) and arg < 0:
                    print(msg.format(idx + 1, defaultValue))
                    newArgs[-1] = defaultValue
            return func(*newArgs, **kwargs)
        return __wrapper
    return __decorator

@check_input_rules(0)
def my_func(a,b,c):
    print(a + b + c)

my_func(1,2,3)
my_func(1,-1,3)
