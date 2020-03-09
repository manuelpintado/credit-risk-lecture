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
                raise

        return wrapper

    return decorator


def load_file(filename):
    with open(filename, "r") as file:
        data = json.loads(file.read())
    return data


def flatten_dict(d, parent_key='', separator='.'):
    items = []
    index = 0
    if isinstance(d, dict):
        for n, (k, v) in enumerate(d.items()):
            new_key = parent_key + str(separator) + k if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, separator=separator).items())
            if isinstance(v, list):
                items.extend(flatten_dict(v, new_key, separator=separator).items())
                index += 1
            else:
                items.append((new_key, v))
    elif isinstance(d, list):
        for k, v in enumerate(d):
            new_key = parent_key + str(separator) + str(k) if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, separator=separator).items())
            if isinstance(v, list):
                items.extend(flatten_dict(v, new_key, separator=separator).items())
                index += 1
            else:
                items.append((new_key, v))
    return dict(items)


def flatten(dictionary):
    return {k: v for k, v in dictionary.items() if not isinstance(v, dict or list)}
