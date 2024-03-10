def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error_message:
            return str(error_message)
        except TypeError as error_message:
            return str(error_message)
    return inner
