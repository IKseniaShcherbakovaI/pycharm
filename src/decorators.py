import time


def log(filename=""):
    """
    Декортаор логирующий начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """

    def my_decorator(func):
        def wrapper(*args, **kwargs):

            try:
                time_1 = time.time()
                result = func(*args, **kwargs)
                time_2 = time.time()
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"start time: {time_1}\n")
                        file.write(f"{func.__name__} ok\n")
                        file.write(f"end time: {time_2}\n")
                        file.write(f"result: {result}\n")
                        print(result)
                    return result
                else:
                    print(f"start time: {time_1}")
                    print(f"{func.__name__} ok")
                    print(f"end time: {time_2}")
                    print(result)

            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args} {kwargs}")

        return wrapper

    return my_decorator


@log(filename="")
def my_function(x, y):
    return x + y

my_function(2, 2)