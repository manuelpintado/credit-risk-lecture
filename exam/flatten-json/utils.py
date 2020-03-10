import functools
import json


def pretty_print(logger, serializer_function=lambda obj: obj.__dict__):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            serializable_obj = func(*args, **kwargs)
            try:
                formatted_output = json.dumps(serializable_obj, indent=4, default=serializer_function)
                print(formatted_output)
            except TypeError as e:
                logger.error("Type Error encounter with message {error}".format(error=e))
                raise  # Re-throw exception to fail the program execution with stack-trace.
        return wrapper
    return decorator


def replace_list_elements(obj):
    if isinstance(obj, list):
        return {str(i): replace_list_elements(v) for i, v in enumerate(obj)}
    if isinstance(obj, dict):
        return {k: replace_list_elements(v) for k, v in obj.items()}
    return obj


def flatten_dict(dictionary, sep=".", prefix=""):
    flat_dict = {}
    for key, val in dictionary.items():
        flat_key = "{prefix}{sep}{key}".format(prefix=prefix, sep=sep, key=key) if prefix else key
        flat_dict = {
            **flat_dict,
            **(flatten_dict(dictionary=val, sep=sep, prefix=flat_key) if isinstance(val, dict) else {flat_key: val})
        }
    return flat_dict
