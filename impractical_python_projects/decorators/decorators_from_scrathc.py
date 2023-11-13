def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        res = func()
        print("Something is happening after the function is called.")
        print(f'from say_hello {res}')

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
    return 1


if __name__ == '__main__':
    print("I am the best")
    say_hello()
