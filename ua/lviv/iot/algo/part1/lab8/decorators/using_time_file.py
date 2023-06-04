import datetime
import functools

def using_time_file(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = func.__name__

        with open("call_history.txt", "a") as file:
            file.write(f"Method {func_name} opened at {time}\n")
        
        return func(*args, **kwargs)

    return wrapper
