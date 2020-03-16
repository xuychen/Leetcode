def get_len(value):
    return "{0:b}".format(value).count('1')

def binary_sort(elements):
    return sorted(elements, key=lambda item: (get_len(item), item))