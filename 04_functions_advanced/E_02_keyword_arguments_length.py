def kwargs_length(**kwargs):
    len_kwargs = len(kwargs)
    return len_kwargs


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
