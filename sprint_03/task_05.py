# Create decorator logger. The decorator should print to the console
# information about function's name and all its arguments separated with
# ',' for the function decorated with logger.
#
# Create function concat with any numbers of any arguments which
# concatenates arguments and apply logger decorator for this function.
#
# For example
#
# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23
#
# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2
#
# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# onetwo


def logger(fn):
    def wrapper(*args, **kwargs):

        lst_args = []
        for a in list(args) + list(kwargs.values()):
            lst_args.append(str(a))

        if fn.__qualname__ == "print_arg":  # <== workaround!
            print(fn(*args, **kwargs))

        print(f"Executing of function {fn.__qualname__} with arguments {', '.join(lst_args)}...")
        return fn(*args, **kwargs)

    return wrapper

@logger
def concat(*args, **kwargs):
    res = ""
    for x in list(args) + list(kwargs.values()):
        res += f"{x}"
    return res

@logger
def sum(*args, **kwargs):
    res = 0
    for x in list(args) + list(kwargs.values()):
        res += x
    return res


@logger
def print_arg(x):
    return x

