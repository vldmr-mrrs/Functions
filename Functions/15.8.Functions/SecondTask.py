func = lambda x: True if str(x[0]).lower() == 'a' and str(x[-1]).lower() == 'a' else False

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))