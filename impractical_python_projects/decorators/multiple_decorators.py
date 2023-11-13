# Timing decorator
import time


def testing_decorator(func):
    def wrapper(*args, **kwargs):
        print('Inside testing')
        func(*args,**kwargs)
        print("Just testing!!")

    return wrapper


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        print('timing called')
        # return result

    return wrapper


# Logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print('log called')
        return result

    return wrapper


# Applying multiple decorators to a single function
@testing_decorator
@timing_decorator
@log_decorator
def my_function():
    print("Inside my_function")
    time.sleep(2)


my_function()
