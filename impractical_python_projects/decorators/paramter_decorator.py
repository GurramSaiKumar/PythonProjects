def custom_calculation(func):
    def wrapper(*args, **kwargs):
        result = 0
        for i in range(0, len(args)):
            result += args[i]
        func(*args)
        return result

    return wrapper


def custom_calculation_with2args(id, name):
    def decorator(func):
        def wrapper(*args):
            if id == 0:
                return f'result is {args[0] + args[1]} for {name}'
            elif id == 1:
                return f'result is {args[0] * args[1]} for {name}'
            func(*args)

        return wrapper

    return decorator


@custom_calculation_with2args(1, 'sai')
def calculate(*args):
    print("No Calculation done!!")


res = calculate(2, 4)
print(f'Result is {res}')
