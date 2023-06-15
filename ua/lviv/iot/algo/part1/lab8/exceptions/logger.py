import logging


def loggering(exception, mode):
    """
    If some exception raise, write a msg of error to console or file, depends on {mode}

    :param: mode - write msg to console or file
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as excep:
                logger = logging.getLogger(func.__name__)
                logger.setLevel(logging.ERROR)

                if mode == "console":
                    console_mode = logging.StreamHandler()
                    console_mode.setLevel(logging.ERROR)
                    if logger.hasHandlers():
                        logger.handlers[0] = console_mode
                    else:
                        logger.addHandler(console_mode)
                elif mode == "file":
                    file_mode = logging.FileHandler("error_handler.log")
                    file_mode.setLevel(logging.INFO)
                    if logger.hasHandlers():
                        logger.handlers[0] = file_mode
                    else:
                        logger.addHandler(file_mode)
                else:
                    raise ValueError("Invalid mode")

                logger.error(str(excep))

        return wrapper
    return decorator
