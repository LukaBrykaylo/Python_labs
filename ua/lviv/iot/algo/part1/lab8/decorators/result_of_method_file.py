import functools

def result_of_method_file(func):

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func_class = self.__class__.__name__
        func_name = func.__name__

        with open(f"{func_class}_{func_name}.txt", "a") as file:
            for x in func(self, *args, **kwargs):
                file.write(f"{x}\n")
            file.write("\n")
        return func(self, *args, **kwargs)
    
    return wrapper
