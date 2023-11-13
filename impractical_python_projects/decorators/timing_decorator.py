import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        local_res = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return local_res + ' 3'

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)
    return '2'


# Call the slow_function and see the timing in action.
res = slow_function()
print(f'res is {res}')
