from collections import OrderedDict

d = {'a': 1, 'd': 4, 'b': 2, 'c': 3}
print(d)

sorted(d.items(), key=lambda x: x[1])
print(d)
