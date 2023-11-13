def log_decorator(func):
    def wrapper(*args, **kwargs):
        for key, val in kwargs.items():
            kwargs[key] = val + ' changed'
        result = func(*args, **kwargs)
        # Add code to log a message after the function call.
        return result

    return wrapper


@log_decorator
def add(*args, **kwargs):
    for key, val in kwargs.items():
        print(f'key is {key} and value is {val}')
    return args[0] + args[1]


# Call the add function and see the logging in action.
result = add(3, 5, a='apple', b='banana')
print("Result:", result)
