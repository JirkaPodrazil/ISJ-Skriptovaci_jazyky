import collections
my_counter = collections.Counter()     
    
def log_and_count(*args_2, **kwargs_2):
    def decorator(func):
        def inner(*args, **kwargs):
            if ("key" in kwargs_2):
                kwargs_2["counts"][kwargs_2["key"]] += 1
            print("called {0} with {1} and {2}".format(func.__name__, args, kwargs))
            return func(*args, **kwargs)
        return inner
    return decorator  


@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b


f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)
