from collections import abc
def double(x: abc.Sequence):
    return x * 2

# print(double(2))
print(double([1, 2, 3]))  # For sequences like lists
