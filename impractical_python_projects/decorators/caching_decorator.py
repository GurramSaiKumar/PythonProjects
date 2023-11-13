def caching_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result

    return wrapper


@caching_decorator
def expensive_calculation(x, y):
    print("Performing expensive calculation...")
    return x + y


result1 = expensive_calculation(3, 5)
result2 = expensive_calculation(3, 5)

print("Result 1:", result1)
print("Result 2:", result2)
