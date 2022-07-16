def func_apply(operation, items):
    result = []
    for i in items:
        result.append(operation(i))
    return result
