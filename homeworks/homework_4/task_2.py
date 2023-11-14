
def key_params(**kwargs):
    params = {}
    for key, value in kwargs.items():
        try:
            if value is None:
                params[str(value)] = key
            else:
                params[value] = key
        except TypeError:
            params[str(value)] = key

    return params


params = key_params(a=None, b='hello', c=[1, 2, 3], d={})
print(params)